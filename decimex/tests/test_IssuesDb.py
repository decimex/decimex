from decimex.IssuesDb import IssuesDb

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

    with db.get_session() as session:
        # db.add_issue(session)
        # db.add_issue(session)
        # db.get_all_issues(session)
        # db.get_first_issue(session)
        # db.delete_issue(session)
        # db.commit_session(session)
        # db.get_all_issues(session)
        print(session)