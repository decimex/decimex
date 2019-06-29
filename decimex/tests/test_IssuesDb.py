from decimex.IssuesDb import IssuesDb
import datetime

def test_sanity():
    db_type     = "postgres"
    user_name   = "admin"
    password    = "Aa123456"
    host        = "localhost"
    port        = "5432"
    db_name     = "issues"

    db = IssuesDb(db_type, user_name, password, host, port, db_name)
    db.initialize()
    db.create_defined_tables()

    repository = "sensu"
    issue_number = 14
    link = "https://github.com/sensu/sensu/baba"
    status = "closed"
    creation_time = datetime.datetime.now()
    close_time = datetime.datetime.now()
    labels = "bug, shug, doug"
    filename = "bla.py"
    good_code = "import kaka"
    bad_code = "import kiki"

    with db.get_session() as session:
        db.add_issue(session, repository, issue_number, link, status, creation_time, close_time, labels)
        db.commit_session(session)
        print(db.get_all_issues(session))

        for issue in db.get_all_issues(session):
            db.delete_issue(session, issue.id)
        db.commit_session(session)
        print(db.get_all_issues(session))

        db.add_issue_file_change(session, issue_number, filename, good_code, bad_code)
        db.commit_session(session)
        print(db.get_all_issue_file_changes(session))

        for issue_file_change in db.get_all_issue_file_changes(session):
            db.delete_issue_file_change(session, issue_file_change.id)
        db.commit_session(session)
        print(db.get_all_issue_file_changes(session))

