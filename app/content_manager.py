import os
import re
import string

class ContentManager:
    def __init__(self, number_of_projects):
        self.run_number = int(os.getenv('GITHUB_RUN_NUMBER'))
        self.number_of_projects = number_of_projects

    def get_run_number(self):
        return self.run_number

    def get_project_index(self):
        return self.run_number % self.number_of_projects

    def read_project_content(self):
        file_index = self.get_project_index()
        file_path = f'content/text/{file_index}.txt'
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

    def read_project_hashtags(self):
        file_index = self.get_project_index()
        file_path = f'content/hashtags/{file_index}.txt'
        try:
            with open(file_path, 'r') as file:
                return ' '.join([line.strip() for line in file.readlines()])
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

    def get_project_image_path(self):
        file_index = self.get_project_index()
        # Updated to point to a .png file instead of .txt
        file_path = f'https://github.com/Dmitrii-Zavalin-Deployments/ePublisher/blob/main/content/images/{file_index}.png?raw=true'
        return file_path

    def get_run_division(self):
        return self.run_number // self.number_of_projects

    def split_into_sentences(self, content):
        # This regex pattern aims to split the text into sentences ending with . ! ? or "
        pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!|")\s'
        sentences = re.split(pattern, content)
        return [sentence.strip() for sentence in sentences if sentence]

    def select_sentence(self):
        sentences = self.split_into_sentences(self.read_project_content())
        num_sentences = len(sentences)
        if num_sentences == 0:
            return None
        selected_index = self.get_run_division() % num_sentences
        return sentences[selected_index]

    def get_hashtagged_words(self, sentence):
        if not sentence:
            return []
        words = sentence.split()
        hashtagged_words = ['#' + word.strip(string.punctuation) for word in words if len(word.strip(string.punctuation)) >= 4]
        return hashtagged_words

    def prepare_post_message(self, additional_hashtags):
        # Declare a new variable to keep text
        post_message = ''
        # Add the text from read_project_content to the variable
        content = self.read_project_content()
        if content:
            post_message += content
        # Add a new line
        post_message += '\n'
        # Add the return from the function read_project_hashtags to the variable
        hashtags = self.read_project_hashtags()
        if hashtags:
            post_message += hashtags
        # Add additional hashtags if any
        if additional_hashtags:
            post_message += ' ' + ' '.join(additional_hashtags)
        # Return the variable
        return post_message

    def create_post_data(self, project_image_path, post_message):
        return {
            'project_image_path': project_image_path,
            'post_message': post_message
        }

    def get_text_before_hashtag(text):
        # Split the text at the first hashtag
        parts = text.split('#', 1)
        # Return the part before the hashtag, or the entire text if no hashtag is found
        return parts[0].strip() if len(parts) > 1 else text.strip()
