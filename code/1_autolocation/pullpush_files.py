import os
import shutil
import json

from globals import DOWNLOADS_FOLDER
from send2 import get_send2person, clean_send2person

def get_json_files():
    json_files = []
    # Iterate over all files in the directory
    for root, dirs, files in os.walk(DOWNLOADS_FOLDER):
        for file in files:
            # Check if the file has a .json extension
            if file.endswith(".json"):
                # Append the absolute path of the file to the list
                json_files.append(os.path.join(root, file))
    return json_files

def get_id(entry):
    return entry.get('id', None)

def mv_input_files(entry):
    input_files = entry.get('input_files', [])
    for file in input_files:
        # Build the origin path.
        origin = os.path.join(DOWNLOADS_FOLDER, os.path.basename(file))
        # Copy the file from request's folder to the destination.
        shutil.move(origin, file)
        print(f"File '{origin}' copied to '{file}'")

def run_input_files(entry):
    input_files = entry.get('input_files', [])
    for file in input_files:
        print(f"{file} run succesfully!")

def mv_output_files(entry, send2person):
    output_files = entry.get('output_files', [])
    for file in output_files:
        destiny = os.path.join(send2person, os.path.basename(file))
        # Copy the file from request's folder to the destination.
        shutil.copyfile(file, destiny)
        print(f"File '{file}' copied to '{destiny}'")


def process_requests(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    for entry in data:
        # Clean send2folders.
        id = get_id(entry)
        send2person = get_send2person(id)
        clean_send2person(send2person)
        print(f"{send2person} was cleaned!")
        # Push-Run-Pull-Zip
        mv_input_files(entry)
        run_input_files(entry)
        mv_output_files(entry, send2person)
        