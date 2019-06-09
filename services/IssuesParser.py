class IssuesParser:
    def parse_issue(self, issue):
        result = []
        if not issue.pull_request:
            return
        pr = issue.as_pull_request()
        files = pr.get_files()
        for file in files:
            result.append(self.process_pr_file(file))
        return result

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
