from decimex.IssuesDb import IssuesDb
from services.ProjectsFinder import ProjectsFinder
from services.IssuesFetcher import IssuesFetcher
from services.IssuesParser import IssuesParser


def main():
    db_type = "postgres"
    user_name = "admin"
    password = "Aa123456"
    host = "localhost"
    port = "5432"
    db_name = "issues"
    projects_finder = ProjectsFinder()
    issues_fetcher = IssuesFetcher()
    issues_db = IssuesDb(db_type, user_name, password, host, port, db_name)
    issues_db.create_defined_tables()
    issues_parser = IssuesParser(issues_db)

    python_repos = projects_finder.search_python_repos()

    for repo in python_repos:
        issues = issues_fetcher.get_issues_from_github(repo)

        for issue in issues:
            issues_parser.parse_issue(issue)
            break

        break


if __name__ == '__main__':
    main()
