import os

class ContentManager:
    def __init__(self):
        # Load content from files
        self.run_id = os.getenv('GITHUB_RUN_ID')

    def get_run_id(self):
        # Return the current run ID
        return self.run_id
