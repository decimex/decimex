from decimex.IssuesDb import Issue, IssueFileChange


class IssuesParser:
    def __init__(self, issues_db):
        """

        :param issues_db:
        :type issues_db: decimex.IssuesDb.IssuesDb
        """
        self.issues_db = issues_db

    def parse_issue(self, issue):
        """

        :param issue:
        :type issue: github.Issue.Issue
        :return:
        """
        file_changes = []
        if not issue.pull_request:
            return
        pr = issue.as_pull_request()
        files = pr.get_files()
        for file in files:
            file_changes.append(self.process_pr_file(file))

        with self.issues_db.get_session() as session:

            db_issue = Issue()
            db_issue.link = issue.url
            db_issue.issue_number = issue.number
            db_issue.creation_time = issue.created_at
            db_issue.close_time = issue.closed_at
            db_issue.labels = ','.join([l.name for l in issue.labels])
            db_issue.status = issue.state
            db_issue.repository = issue.repository.full_name

            session.add(db_issue)
            session.commit()
            for file_change in file_changes:
                db_file_change = IssueFileChange()
                db_file_change.issue_id = db_issue.id
                db_file_change.filename = file_change['name']
                db_file_change.good_code = file_change['good_code']
                db_file_change.bad_code = file_change['bad_code']
                session.add(db_file_change)
            session.commit()
        return db_issue

    @staticmethod
    def process_pr_file(pr_file):
        good_code = ''
        bad_code = ''
        for line in pr_file.patch.splitlines():
            if not line.startswith('+'):
                bad_code += line
            if not line.startswith('-'):
                good_code += line
        return {'name': pr_file.filename, 'good_code': good_code, 'bad_code': bad_code}



