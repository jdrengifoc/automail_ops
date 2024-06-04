import init
import credentials
from global_variables import *

def init_main():
    init.initialize_folder(SEND2_FOLDER)
    init.initialize_folder(SECURE_FOLDER)
    init.initiallize_collaborators_json(COLABORATORS_FILE)
    init.initiallize_collaborators_dataframe(COLABORATORS_FILE2)
    init.init_logs_history_parquet(LOGS_HISTORY_FILE)
    print("Initialization completed successfully.")

# Check if the script is being run directly.
if __name__ == "__main__":
    init_main()
    credentials.add_collaborator(
        'Juan', 'jdrengifoc@eafit.edu.co', ['./src'], ['./src/init.py'])
    credentials.get_collaborators_info('name')
    credentials.update_credential_by_name(
        'jUAN', 'juanda', 'jdrengifoc@eafit.edu.co',
        ['./src'], ['./src/init.py'])
    credentials.update_credential_by_name(
        'JUANDA', 'juan Rengifo', 'jdrengifoc13@gmail.com',
        ['./src'], ['./src/init.py'])