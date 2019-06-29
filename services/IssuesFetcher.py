from github import Github


class IssuesFetcher:
    def get_issues_from_github(self, repo, status="closed"):
        bug_label = None
        for label in repo.get_labels():
            if 'bug' in label.name.lower():
                bug_label = label
                break

        # TODO: filter by time
        if bug_label is None:
            issues = repo.get_issues(state=status)
        else:
            issues = repo.get_issues(state=status, labels=[bug_label])

        resolved_issues = []
        for i in range(10):
            try:
                resolved_issues.append(issues[i])
            except IndexError:
                pass

        return resolved_issues
