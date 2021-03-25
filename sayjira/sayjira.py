import sys
import re

from pathlib import Path

import git


def get_jira_ticket(branch_name):
    jira_ticket = re.match(r"((?<!([A-Z]\{1,10\})-\?)[A-Z]+-\d+)", branch_name)
    if jira_ticket:
        return jira_ticket.group(0)

    
def update_commit_message(branch, jira_ticket):
    message_path = sys.argv[1]
    with open(message_path, "rw") as message_file:
        message = message_file.read()
        message_file.write(f"[{jira_ticket}] {message}")


def main():
    repo = git.Repo(".")
    branch = repo.head.reference
    jira_ticket = get_jira_ticket(branch.name)
    if jira_ticket:
        update_commit_message(branch, jira_ticket)
    

if __name__ == '__main__':
    sys.exit(main())
