from ..consts import GITHUB_ACCESS_TOKEN
from github import Github

class ProjectsFinder():
    def __init__(self):
        self.should_run = False

    def start(self):
        self.should_run = True

        while self.should_run:
            self._run()

    def stop(self):
        self.should_run = False

    def _run(self):
        self.get_random_repos()
        sleep(1)

    def search_python_repos(self):
         python_repos = g.search_repositories(query='language:python')
