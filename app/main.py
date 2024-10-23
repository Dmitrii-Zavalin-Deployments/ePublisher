import subprocess
import os
from epublisher_facebook_manager import EPublisherFacebookManager
from content_manager import ContentManager
from text_generator import generate_text

def main():
    # Initialize managers
    content_manager = ContentManager(number_of_projects=int(os.getenv('NUMBER_OF_PROJECTS')))
    epublisher_facebook_manager = EPublisherFacebookManager()

    # Log file paths
    log_file_texts = 'generated_content.log'
    log_file_hashtags = 'generated_content.log'

    # Get Run Number
    run_number = str(content_manager.get_run_number())
    print(f"The current run ID is: {run_number}")

    # Calculate the project index for the current run
    project_index = str(content_manager.get_project_index())
    print(f"Current project's to post index: {project_index}")

    # Read unchangeable hashtags
    unchangeable_hashtags = content_manager.read_project_hashtags()
    if unchangeable_hashtags is not None:
        print(f"Unchangeable Project hashtags:\n{unchangeable_hashtags}")
        unchangeable_hashtags_length = len(unchangeable_hashtags)
    else:
        unchangeable_hashtags_length = 0
    print(f"Length of unchangeable hashtags: {unchangeable_hashtags_length}")

    # Calculate allowed length for the new text
    allowed_text_length = (50 - unchangeable_hashtags_length) // 4
    print(f"Allowed length for the new text: {allowed_text_length}")

    # Generate new project text
    original_text = content_manager.read_project_content()
    if original_text is not None:
        print(f"Original Project text:\n{original_text}")
        project_text = generate_text(original_text, length=allowed_text_length, log_file=log_file_texts)
        print(f"New Project text:\n{project_text}")
    else:
        project_text = ""

    # Read and print the project link
    project_link = content_manager.read_project_links()
    if project_link is not None:
        print(f"Project link:\n{project_link}")
    else:
        project_link = ""

    # Combine project_text, project_link, and all_hashtags into project_content
    project_content = f"{project_link} {project_text} {unchangeable_hashtags}".strip()
    print(f"Project content:\n{project_content}")

    # Get the project image path
    project_image_path = content_manager.get_project_image_path()
    print(f"Project image path:\n{project_image_path}")

    # Calculate and print the integer division of run_number by number_of_projects
    run_division = str(content_manager.get_run_division())
    print(f"Integer division of run number by number of projects: {run_division}")

    # Prepare and print the post message with all hashtags
    post_message = f"{project_content}"
    print(f"Post message:\n{post_message}")

    # Create post data and print it
    post_data = content_manager.create_post_data(project_image_path, post_message)
    print("Post Data:")
    print(post_data)

    # Extract image path and text content from post_data
    image_path = post_data['project_image_path']
    text_content = post_data['post_message']

    # Summarize the text and update the content file
    content_manager.summarize_and_update_text(content_before_hashtag=project_text)

    # Commented out block for Facebook and Twitter posting
    """
    try:
        # New: Get and print the Facebook posts
        facebook_posts = epublisher_facebook_manager.get_facebook_posts()
        print(f"Facebook posts:\n{facebook_posts}")

        # Searching for posts to delete
        message_ids = epublisher_facebook_manager.print_message_before_hashtag(facebook_posts, content_before_hashtag)

        # Delete post with message_ids
        deleted_post = epublisher_facebook_manager.delete_facebook_posts(message_ids)
        print('Repeated posts are deleted')

        # Post in Facebook
        epublisher_facebook_manager.post_to_facebook(image_path, text_content)

    except Exception as e:
        print("Failed to post on Facebook: ", e)

    # Call the Node.js script with the parameters to start Twitter
    subprocess.run(['node', 'js/tweet.js', image_path, text_content, content_before_hashtag], check=True)
    """

if __name__ == "__main__":
    main()