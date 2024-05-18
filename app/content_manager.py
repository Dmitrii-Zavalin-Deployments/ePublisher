import os

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

    def read_project_images(self):
        file_index = self.get_project_index()
        file_path = f'content/images/{file_index}.txt'
        try:
            with open(file_path, 'r') as file:
                # Assuming the file contains a direct link to the image
                return file.read().strip()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
