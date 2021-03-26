import sys
import re
import argparse

from pathlib import Path

import git


repo = git.Repo(".")


def get_jira_ticket(branch_name):
    jira_ticket = re.match(r"((?<!([A-Z]\{1,10\})-\?)[A-Z]+-\d+)", branch_name)
    if jira_ticket:
        return jira_ticket.group(0)


def update_commit_message(message, jira_ticket):
    with open(message, "w") as message_file:
        message_text = message_file.read()
        message_file.write(f"[{jira_ticket}] {message_text}")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+")
    args = parser.parse_args(argv)
    branch = repo.head.reference
    jira_ticket = get_jira_ticket(branch.name)
    if jira_ticket:
        update_commit_message(args.filenames[0], jira_ticket)
    

if __name__ == '__main__':
    sys.stderr.write("This hook works")
    sys.exit(main())
