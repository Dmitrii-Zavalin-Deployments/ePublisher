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
    
    # Read and print the project hashtags
    project_hashtags = content_manager.read_project_hashtags()
    if project_hashtags is not None:
        print(f"Project hashtags:\n{project_hashtags}")
        
    # Get the project image path
    project_image_path = content_manager.get_project_image_path()
    print(f"Project image path:\n{project_image_path}")
    
    # Prepare and print the post message
    post_message = content_manager.prepare_post_message()
    print(f"Post message:\n{post_message}")

    # Calculate and print the integer division of run_number by number_of_projects
    run_division = content_manager.get_run_division()
    print(f"Integer division of run number by number of projects: {run_division}")

if __name__ == "__main__":
    main()
