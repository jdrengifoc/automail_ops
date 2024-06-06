import os
import json
import pandas as pd
import pyarrow as pa

from global_variables import *

def initialize_folder(folder: str) -> None:
    """
    Initializes folders with specific files.

    Args:
    - folder (str): Path to the folder.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder {folder}")
    else:
        print(f'{folder} already exists.')

def initiallize_collaborators_json(file_name: str) -> None:
    """
    Initializes a JSON file for storing collaborators' information.

    Args:
        file_name (str): The name of the JSON file.
    """
    full_path = os.path.join(SECURE_FOLDER, file_name)
    if not os.path.exists(full_path):
        with open(full_path, 'w') as f:
            json.dump([], f)
    else:
        print(f'{full_path} already exists.')

def initiallize_collaborators_dataframe(file_name: str) -> None:
    """
    Initializes a JSON file for storing collaborators' information.

    Args:
        file_name (str): The name of the JSON file.
    """
    full_path = os.path.join(SECURE_FOLDER, file_name)
    if not os.path.exists(full_path):
        df = pd.DataFrame(columns=['id', 'send2folder', 'name', 'emasil', 'allowed_folders'])
        df.to_csv(full_path)
    else:
        print(f'{full_path} already exists.')

def init_logs_history_parquet(file_name: str) -> None:
    """
    Initializes a Parquet file for storing logs history.

    Args:
        file_name (str): The name of the Parquet file.
    """
    full_path = os.path.join(SECURE_FOLDER, file_name)
    if not os.path.exists(full_path):
        schema = pa.schema([
            ('id', pa.int64()),
            ('id_email', pa.int64()),
            ('date', pa.timestamp('ns')),
            ('step', pa.string()),
            ('exit_status', pa.string())
            ])
        df = pd.DataFrame(columns=[field.name for field in schema])
        df.to_parquet(
            full_path, engine='pyarrow', compression=None, index=False, schema=schema
            )
    else:
        print(f'{full_path} already exists.')