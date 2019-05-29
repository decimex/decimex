from services.ProjectsFinder import ProjectsFinder
from services.IssuesFetcher import IssuesFetcher
from services.IssuesParser import IssuesParser


def main():
    projects_finder = ProjectsFinder()
    issues_fetcher = IssuesFetcher()
    issues_parser = IssuesParser()

    python_repos = projects_finder.search_python_repos()

    for repo in python_repos:
        issues = issues_fetcher.get_issues_from_github(repo)

        for issue in issues:
            issues_parser.parse_issue(issue)

if __name__ == '__main__':
    main()
