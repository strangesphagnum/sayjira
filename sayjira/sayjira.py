import sys
import re

from pathlib import Path

import git


repo = git.Repo(".")


def get_jira_ticket(branch_name):
    jira_ticket = re.match(r"((?<!([A-Z]\{1,10\})-\?)[A-Z]+-\d+)", branch_name)
    if jira_ticket:
        return jira_ticket.group(0)

    
def update_commit_message():
    commit = repo.head.commit
    branch.commit = commit.parents[0]
    print(branch.commit)
    # new_message = repo.index.commit(f"new message")


def main(argv=None):
    branch = repo.head.reference
    jira_ticket = get_jira_ticket(str(branch))
    if jira_ticket:
        update_commit_message()
    

if __name__ == '__main__':
    sys.exit(main())
