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


def update_commit_message(commit, jira_ticket):
    print(message)
    with open(commit, "w") as commit_file:
        commit_content = commit_file.readlines()
        message_text = commit_content[0]
        commit_content[0] = (f"[{jira_ticket}] {message_text}")
        commit_file.writelines(commit_content)


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
