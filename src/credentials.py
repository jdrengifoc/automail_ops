import os
import json
import uuid
import re

from global_variables import *
from auxiliars import bidirectional_subset, clean_string, get_matching_index

# Get collaborators related information.
def get_collaborators() -> list[dict]:
    file_path = os.path.join(SECURE_FOLDER, COLABORATORS_FILE)

    if not os.path.exists(file_path):
        raise ValueError(f"{file_path} has not been initialized.")
    with open(file_path, 'r') as f:
        return json.load(f)

def get_collaborators_info(field: str) -> list:
    collaborators = get_collaborators()
    return [collaborator.get(field) for collaborator in collaborators]

# Controls.
def duplicates_control(new_credential: dict) -> None:
    # Unpack control varaibles.
    id = new_credential['id']
    name = new_credential['name']
    email = new_credential['email']
    
    # Search duplicates.
    for collaborator in get_collaborators():
        if collaborator['id'] == id:
            continue
        elif collaborator['name'] == name:
            raise ValueError(f"{name} is already registered.")
        elif collaborator['email'] == email:
            raise ValueError(f"{email} is already registered.")
        
def validate_email(email: str) -> None:
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'
    if not re.fullmatch(regex, email):
        raise ValueError(f"Invalid email: {email}.")
 
def validate_paths(paths) -> None:
    for path in paths:
        if not os.path.exists(path):
            raise ValueError(f"{path} doesn't exists.")
        
def check_mutable_keys(credential: dict):
    expected_keys = ['send2folder', 'name', 'email', 'allowed_folders', 'allowed_files']
    credential_keys = list(credential.keys())
    if 'id' in credential_keys:
        credential_keys.remove('id')

    if not bidirectional_subset(expected_keys, credential_keys):
        raise ValueError(
            f"Incorrect credential key names, is expected {expected_keys} and recieved {credential_keys}.")

def validate_mutable_credentials(credential: dict):
    check_mutable_keys(credential)
    validate_email(credential['email'])
    validate_paths(credential['allowed_folders'])
    validate_paths(credential['allowed_files'])
    duplicates_control(credential)

# Auxiliary functions to mutate collaborators database   
def generate_new_id() -> str:
    current_ids = get_collaborators_info('id')
    new_id = str(uuid.uuid4())
    while new_id in current_ids:
        new_id = str(uuid.uuid4())

    return new_id

def create_mutable_credential(
        name: str, email: str, allowed_folders: list[str], allowed_files: list[str]) -> dict:
    credential = {
        'send2folder': os.path.join(SEND2_FOLDER, f'send2{clean_string(name.lower())}'),
        'name': name.lower(),
        'email': email.lower(),
        'allowed_folders': allowed_folders,
        'allowed_files': allowed_files
    }
    return credential

def update_collaborators(collaborators: list[dict]) -> None:
    file_path = os.path.join(SECURE_FOLDER, COLABORATORS_FILE)
    with open(file_path, 'w') as f:
        json.dump(collaborators, f, indent=4)
    print(f"{file_path} succesfully updated.")



def add_collaborator(
        name: str, email: str, allowed_folders: list[str], allowed_files: list[str]) -> None:
    """
    Adds a new person to the JSON file if the name or email isn't already in the file.

    Args:
        name (str): Name of the person.
        email (str): Email of the person.
        person_id (int): ID of the person.
        allowed_folders (list of str): A list of folders that the person is allowed to access.
        allowed_files (list of str): A list of files that the person is allowed to access.
    """
    collaborators = get_collaborators()
    
    new_credentials = create_mutable_credential(name, email, allowed_folders, allowed_files)
    new_credentials['id'] = generate_new_id()
    validate_mutable_credentials(new_credentials)
    
    # Add new credentials.
    os.mkdir(new_credentials['send2folder'])
    collaborators.append(new_credentials)
    update_collaborators(collaborators)

def update_credential_by_name(
        current_name: str, name: str, email: str, 
        allowed_folders: list[str], allowed_files: list[str]) -> None:
    
    # Controls
    current_name = current_name.lower()
    if not current_name in get_collaborators_info('name'):
        raise ValueError(f"There is no collaborator named {current_name}.")

    # Update collaborator mutatable info.
    new_credential = create_mutable_credential(name, email, allowed_folders, allowed_files)
    collaborators = get_collaborators()
    for i, collaborator in enumerate(collaborators):
        if collaborator.get('name') == current_name:
            new_credential['id'] = collaborator['id']
            validate_mutable_credentials(new_credential)
            os.rename(collaborator['send2folder'], new_credential['send2folder'])
            collaborators[i] = new_credential
            break  # Stop searching once the collaborator is found
        
    update_collaborators(collaborators)