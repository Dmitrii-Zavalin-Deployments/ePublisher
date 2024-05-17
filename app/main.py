from epublisher import EPublisherManager
from content_manager import ContentManager

def main():
    # Initialize managers
    epublisher_manager = EPublisherManager()
    content_manager = ContentManager()

    # Script logic
    print(f"The current run ID is: {content_manager.get_run_number()}")

if __name__ == "__main__":
    main()
