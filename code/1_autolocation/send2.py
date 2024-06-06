from globals import SEND2FOLDER
import os
import shutil

def get_send2person(id):
    return os.path.join(SEND2FOLDER, f"send2{id}")

def clean_send2person(send2person):
    if os.path.exists(send2person):
        shutil.rmtree(send2person)
        print("remove dir {send2person}.")
    os.mkdir(send2person)
    
    zip_path = send2person + ".zip"
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"Associated .zip file '{zip_path}' removed.")