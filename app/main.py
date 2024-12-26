import subprocess
import os
from datetime import datetime
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

    # Add a unique hashtag based on the current date and time
    now = datetime.now()
    unique_hashtag = f"#{now.strftime('%Y%m%d%H%M')}"
    unique_hashtag_with_note = f"{unique_hashtag} (AI-generated post)"
    print(f"Generated unique hashtag: {unique_hashtag_with_note}")

    # Read unchangeable hashtags
    unchangeable_hashtags = content_manager.read_project_hashtags()
    if unchangeable_hashtags is not None:
        unchangeable_hashtags += f" {unique_hashtag_with_note}"
        print(f"Unchangeable Project hashtags:\n{unchangeable_hashtags}")
        unchangeable_hashtags_length = len(unchangeable_hashtags)
    else:
        unchangeable_hashtags = unique_hashtag_with_note
        unchangeable_hashtags_length = len(unchangeable_hashtags)
    print(f"Length of unchangeable hashtags: {unchangeable_hashtags_length}")

    # Calculate allowed length for the new text
    allowed_text_length = (140 - unchangeable_hashtags_length) // 4
    print(f"Allowed length for the new text: {allowed_text_length}")

    # Read and print the project link
    project_link = content_manager.read_project_links()
    if project_link is not None:
        print(f"Project link:\n{project_link}")
    else:
        project_link = ""

    # Generate new project text
    original_text = content_manager.read_project_content()
    if original_text is not None:
        print(f"Original Project text:\n{original_text}")
        project_text = generate_text(original_text, length=allowed_text_length, log_file=log_file_texts, link_sentence=project_link)
        print(f"New Project text:\n{project_text}")
    else:
        project_text = ""

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
'''
    # Summarize the text and update the content file
    # content_manager.summarize_and_update_text(content_before_hashtag=project_text)

    try:
        # Post to Instagram
        epublisher_facebook_manager.post_to_instagram(image_path, text_content)
    except Exception as e:
        print("Failed to post on Instagram: ", e)

    try:
        # Post to Facebook
        # epublisher_facebook_manager.post_to_facebook(image_path, text_content)
        print("Posting to Facebook is currently commented out. Please reconnect the business page to the app first.")
    except Exception as e:
        print("Failed to post on Facebook: ", e)

    try:
        # Call the Node.js script with the parameters to start Twitter
        subprocess.run(['node', 'js/tweet.js', image_path, text_content, project_link], check=True)
    except Exception as e:
        print("Failed to post on Twitter: ", e)
'''
if __name__ == "__main__":
    main()