from app.epublisher import EPublisherManager
from app.content_manager import ContentManager

def main():
    # Initialize managers
    epublisher_manager = EPublisherManager()
    # Initialize ContentManager with the number of projects
    content_manager = ContentManager(number_of_projects=int(os.getenv('NUMBER_OF_PROJECTS')))

    # Script logic
    print(f"The current run ID is: {content_manager.get_run_number()}")
    # Calculate the project index for the current run
    project_index = content_manager.get_project_index()
    print(f"Today's project index: {project_index}")

if __name__ == "__main__":
    main()
