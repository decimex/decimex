from services.IssuesFetcher import IssuesFetcher
from services.IssuesParser import IssuesParser


def main():
    parser = IssuesParser()
    issues = IssuesFetcher().get_issues_from_github("zzzeek", 'sqlalchemy')
    for issue in issues:
        parser.parse_issue(issue)

if __name__ == '__main__':
    main()