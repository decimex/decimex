from github import Github

from consts import GITHUB_API_KEY


class IssuesFetcher:
    def get_issues_from_github(self, organization, project, status="closed"):
        github = Github(GITHUB_API_KEY)
        repo = github.get_repo(organization + '/' + project)
        bug_label = None
        for label in repo.get_labels():
            if 'bug' in label.name.lower():
                bug_label = label
                break
        issues = repo.get_issues(state=status, labels=[bug_label])
        for issue in issues:
            print(issue)