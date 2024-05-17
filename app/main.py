from epublisher import EPublisherManager
from content_manager import ContentManager
from file_checker import check_sequential_files, calculate_remainder

def main():
    # Initialize managers
    epublisher_manager = EPublisherManager()
    content_manager = ContentManager()

    # Script logic
    print(f"The current run ID is: {content_manager.get_run_number()}")
    directories = [
        'ePublisher/content/hashtags',
        'ePublisher/content/images',
        'ePublisher/content/text'
    ]
    missing_files = check_sequential_files(directories)
    if not any(missing_files.values()):
        print("All sequential files are present.")
    else:
        print(f"Missing files: {missing_files}")

    run_number = int(content_manager.get_run_number())
    max_number = max(get_max_file_number(directory) for directory in directories)
    remainder = calculate_remainder(run_number, max_number)
    print(f"The remainder of dividing the run number by the maximum file number is: {remainder}")

if __name__ == "__main__":
    main()
