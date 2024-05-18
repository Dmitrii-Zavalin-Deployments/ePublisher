import os

class ContentManager:
    def __init__(self, number_of_projects):
        self.run_number = int(os.getenv('GITHUB_RUN_NUMBER'))
        self.number_of_projects = number_of_projects

    def get_run_number(self):
        return self.run_number

    def get_project_index(self):
        # Calculate the index for today's project
        return self.run_number % self.number_of_projects

    def read_project_content(self):
        # Determine the file name based on the project index
        file_index = self.get_project_index()
        file_path = f'content/text/{file_index}.txt'
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

    def read_project_hashtags(self):
        # Determine the file name based on the project index
        file_index = self.get_project_index()
        file_path = f'hashtags/text/{file_index}.txt'
        try:
            with open(file_path, 'r') as file:
                # Read hashtags and create a string separated by spaces
                return ' '.join([line.strip() for line in file.readlines()])
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
