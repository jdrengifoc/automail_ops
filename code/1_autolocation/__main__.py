from pullpush_files import get_json_files, process_requests

def main(): 
    requests = get_json_files()
    for request in requests:
        print(request)
        process_requests(request)
        print(f"Request {request} process succesfully!")
        
    


if __name__ == "__main__":
    main()