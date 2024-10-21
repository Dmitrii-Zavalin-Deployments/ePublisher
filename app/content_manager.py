import os
import re
import string
from gpt4all import GPT4All

class ContentManager:
    def __init__(self, number_of_projects):
        self.run_number = int(os.getenv('GITHUB_RUN_NUMBER'))
        self.number_of_projects = number_of_projects
        self.model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

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

    def read_project_links(self):
        file_index = self.get_project_index()
        file_path = f'content/links/{file_index}.txt'
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

    def get_project_image_path(self):
        file_index = self.get_project_index()
        file_path = f'https://github.com/Dmitrii-Zavalin-Deployments/ePublisher/blob/main/content/images/{file_index}.png?raw=true'
        return file_path

    def get_run_division(self):
        return self.run_number // self.number_of_projects

    def split_into_sentences(self, content):
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
        post_message = ''
        content = self.read_project_content()
        if content:
            post_message += content
        post_message += '\n'
        hashtags = self.read_project_hashtags()
        if hashtags:
            post_message += hashtags
        if additional_hashtags:
            post_message += ' ' + ' '.join(additional_hashtags)
        return post_message

    def create_post_data(self, project_image_path, post_message):
        return {
            'project_image_path': project_image_path,
            'post_message': post_message
        }

    def get_text_before_hashtag(self, text):
        parts = text.split('#', 1)
        return parts[0].strip() if len(parts) > 1 else text.strip()

    def update_project_content_with_summary(self, text_to_summarize):
        file_index = self.get_project_index()
        file_path = f'content/text/{file_index}.txt'
        current_content = self.read_project_content() or ""
        summary_prompt = f"Summarize this text and append to current content: {current_content}\n{text_to_summarize}\nSummary:"
        summary = self.model.generate(summary_prompt).strip()
        updated_content = f"{current_content}\n{summary}"
        with open(file_path, 'w') as file:
            file.write(updated_content)