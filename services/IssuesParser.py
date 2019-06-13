class IssuesParser:
    def parse_issue(self, issue):
        result = {}
        file_changes = []
        if not issue.pull_request:
            return
        pr = issue.as_pull_request()
        files = pr.get_files()
        for file in files:
            file_changes.append(self.process_pr_file(file))
        result['creation_time'] = issue.created_at
        result['close_time'] = issue.closed_at
        result['link'] = issue.url
        result['issue_number'] = issue.number
        return file_changes

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
