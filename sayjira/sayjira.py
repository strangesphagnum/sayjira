import sys
import re

from pathlib import Path

import git


repo = git.Repo(".")


def get_jira_ticket(branch_name):
    jira_ticket = re.match(r"((?<!([A-Z]\{1,10\})-\?)[A-Z]+-\d+)", branch_name)
    if jira_ticket:
        return jira_ticket.group(0)


def update_commit_message(message_path, jira_ticket):
    with open(message_path, "r+") as mf:
        message_text = mf.read()
        mf.seek(0, 0)
        mf.write(f"[{jira_ticket}] {message_text}")


def main(argv=None):
    branch = repo.head.reference
    jira_ticket = get_jira_ticket(branch.name)
    if jira_ticket:
        update_commit_message(sys.argv[1], jira_ticket)
    

if __name__ == '__main__':
    sys.exit(main())
