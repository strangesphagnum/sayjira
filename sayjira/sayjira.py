import sys
import re

from pathlib import Path

import git


repo = git.Repo(".")


def get_jira_ticket(branch_name):
    jira_ticket = re.match(r"((?<!([A-Z]\{1,10\})-\?)[A-Z]+-\d+)", branch_name)
    if jira_ticket:
        return jira_ticket.group(0)

    
def update_commit_message(branch, jira_ticket):
    commit = repo.head.commit
    latest_message = branch.commit.message
    branch.commit = commit.parents[0]
    new_message = repo.index.commit(f"[{jira_ticket}] {latest_message}")


def main():
    branch = repo.head.reference
    jira_ticket = get_jira_ticket(branch.name)
    if jira_ticket:
        update_commit_message(branch)
    

if __name__ == '__main__':
    sys.exit(main())
