from services.ProjectsFinder import ProjectsFinder
from services.IssuesFetcher import IssuesFetcher
from services.IssuesParser import IssuesParser


def main():
    projects_finder = ProjectsFinder()
    issues_parser = IssuesParser()
    issues_fetcher = IssuesFetcher()

    issues_fetcher.get_issues_from_github("zzzeek", 'sqlalchemy')

    for issue in issues:
        parser.parse_issue(issue)

if __name__ == '__main__':
    main()
