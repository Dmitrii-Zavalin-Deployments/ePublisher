import os
from epublisher_facebook_manager import EPublisherFacebookManager
from content_manager import ContentManager

def main():
     # Initialize managers
    content_manager = ContentManager(number_of_projects=int(os.getenv('NUMBER_OF_PROJECTS')))
    epublisher_facebook_manager = EPublisherFacebookManager()

    # Get Run Number
    run_number = str(content_manager.get_run_number())
    print(f"The current run ID is: {run_number}")
    
    # Calculate the project index for the current run
    project_index = str(content_manager.get_project_index())
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
    
    # Calculate and print the integer division of run_number by number_of_projects
    run_division = str(content_manager.get_run_division())
    print(f"Integer division of run number by number of projects: {run_division}")

    # Read and print the project content
    project_content = content_manager.read_project_content()
    if project_content is not None:
        print(f"Project content:\n{project_content}")
        # New: Print the list of sentences
        sentences = content_manager.split_into_sentences(project_content)
        print(f"List of sentences:\n{sentences}")

    # Print the selected sentence and informative words for additional hashtags
    selected_sentence = content_manager.select_sentence()
    if selected_sentence is not None:
        print(f"Selected sentence:\n{selected_sentence}")
        hashtagged_words = content_manager.get_hashtagged_words(selected_sentence)
        print(hashtagged_words)

        # Prepare and print the post message with additional hashtags
        post_message = content_manager.prepare_post_message(hashtagged_words)
        print(f"Post message:\n{post_message}")

        # Create post data and print it
        post_data = content_manager.create_post_data(project_image_path, post_message)
        print("Post Data:")
        print(post_data)

    # Extract image path and text content from post_data
    image_path = post_data['project_image_path']
    text_content = post_data['post_message']

    # New: Get and print the Facebook posts
    facebook_posts = epublisher_facebook_manager.get_facebook_posts()
    print(f"Facebook posts:\n{facebook_posts}")

    # Searching for posts to delete
    message_ids = print_message_before_hashtag(facebook_posts)

    # Post in Facebook
    epublisher_facebook_manager.post_to_facebook(image_path, text_content)

if __name__ == "__main__":
    main()
