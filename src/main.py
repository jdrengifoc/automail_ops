import init
import credentials
from global_variables import *

def init_main():
    init.initialize_folder(SEND2_FOLDER)
    init.initialize_folder(SECURE_FOLDER)
    init.initiallize_collaborators_json(COLABORATORS_FILE)
    init.init_logs_history_parquet(LOGS_HISTORY_FILE)
    print("Initialization completed successfully.")

# Check if the script is being run directly.
if __name__ == "__main__":
    init_main()
    #credentials.create_credentials(
    #    'Juan', 'jdrengifoc@eafit.edu.co', ['./src'], ['./src/init.py'])
    collaborators = credentials.get_collaborators()
    credentials.get_collaborators_info(collaborators, 'name')