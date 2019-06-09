class IssuesParser:
    def parse_issue(self, issue):
        result = []
        if not issue.pull_request:
            return
        pr = issue.as_pull_request()
        files = pr.get_files()
        for file in files:
            result.append({'name': file.filename, 'patch': file.patch})
        return result

