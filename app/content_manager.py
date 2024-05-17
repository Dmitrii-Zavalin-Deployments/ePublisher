import os

class ContentManager:
    def __init__(self):
        # Load content from files
        self.run_number = os.getenv('GITHUB_RUN_NUMBER')

    def get_run_number(self):
        # Return the number of this run
        return self.run_number
