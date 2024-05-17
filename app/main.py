import os
from epublisher import EPublisherManager
from content_manager import ContentManager

def main():
    # Initialize managers
    epublisher_manager = EPublisherManager()
    
    # Initialize ContentManager with the number of projects
    content_manager = ContentManager(number_of_projects=int(os.getenv('NUMBER_OF_PROJECTS')))

    # Script logic
    print(f"The current run ID is: {content_manager.get_run_number()}")
    
    # Calculate the project index for the current run
    project_index = content_manager.get_project_index()
    print(f"Current project's to post index: {project_index}")
    
    # Read and print the project content
    project_content = content_manager.read_project_content()
    if project_content is not None:
        print(f"Project content:\n{project_content}")

if __name__ == "__main__":
    main()
