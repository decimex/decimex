from github import Github


class IssuesFetcher:
    def get_issues_from_github(self, repo, status="closed"):
        bug_label = None
        for label in repo.get_labels():
            if 'bug' in label.name.lower():
                bug_label = label
                break

        # TODO: filter by time
        issues = repo.get_issues(state=status, labels=[bug_label])
        issues = list(iter(issues))

        for issue in issues:
            print(issue)
        return issues
