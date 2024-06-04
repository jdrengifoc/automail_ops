import os
import json
import uuid

from global_variables import *

def get_collaborators() -> list[dict]:
    file_path = os.path.join(SECURE_FOLDER, COLABORATORS_FILE)

    if not os.path.exists(file_path):
        raise ValueError(f"{file_path} has not been initialized.")
    with open(file_path, 'r') as f:
        return json.load(f)

def get_collaborators_info(collaborators: list[dict], field: str):
    return [collaborator.get(field) for collaborator in collaborators]
         
def duplicates_control(new_credentials: dict) -> None:
    # Unpack control varaibles.
    name = new_credentials['name']
    email = new_credentials['email']
    
    # Search duplicates.
    for collaborator in get_collaborators():
        if collaborator['name'] == name:
            raise ValueError(f"There is a credential with this {name}.")
        elif collaborator['email'] == email:
            raise ValueError(f"There is a credential with this {email}.")
        
def validate_email(email: str):
    pass

def validate_paths(paths):
    for path in paths:
        if not os.path.exists(path):
            raise ValueError(f"{path} doesn't exists.")
        
def validate_credentials(credentials: dict):
    validate_email(credentials['email'])
    validate_paths(credentials['allowed_folders'])
    validate_paths(credentials['allowed_files'])
    duplicates_control(credentials)

def generate_new_id(collaborators: list[dict]) -> str:
    current_ids = get_collaborators_info(collaborators, 'id')
    new_id = str(uuid.uuid4())
    while new_id in current_ids:
        new_id = str(uuid.uuid4())

    return new_id

def update_collaborators(collaborators: list[dict]) -> None:
    file_path = os.path.join(SECURE_FOLDER, COLABORATORS_FILE)
    with open(file_path, 'w') as f:
        json.dump(collaborators, f, indent=4)
    print(f"{file_path} succesfully updated.")

def create_credentials(
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
    new_credentials = {
        'id': generate_new_id(collaborators),
        'name': name.lower(),
        'email': email.lower(),
        'allowed_folder': allowed_folders,
        'allowed_files': allowed_files
    }
    validate_credentials(new_credentials)
    
    # Add new credentials.
    collaborators.append(new_credentials)
    update_collaborators(collaborators)

def update_credentials_by_name(name: str, new_credentials: dict) -> None:
    """
    Update credentials by searching for a collaborator's name.

    Args:
        name (str): The name of the collaborator to search for.
        new_data (dict): New data to update for the collaborator.
        credentials_file (str): Path to the credentials file.

    Returns:
        None
    """
    name = name.lower()

    collaborators = get_collaborators()
    validate_credentials(new_credentials)
    # Update collaborator info.
    for collaborator in collaborators:
        if collaborator.get('name') == name:
            # Update the collaborator's information with the new data
            collaborator.update(new_credentials)
            break  # Stop searching once the collaborator is found
    
    update_collaborators(collaborators)
    
