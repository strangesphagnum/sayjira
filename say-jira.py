import sys
import re

from pathlib import Path


def get_branch_name():
    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as git:
        content = git.read().splitlines()
        for line in content:
            if "ref:" in line:
                return line.split("/")[-1]


def get_jira_ticket(branch_name):
    jira_ticket = re.match(r"((?<!([A-Z]\{1,10\})-\?)[A-Z]+-\d+)", branch_name)
    if jira_ticket:
        return jira_ticket.group(0)


def main(argv=None):
    branch_name = get_branch_name()
    user_input = sys.argv
    jira_ticket = get_jira_ticket(branch_name)
    if jira_ticket:
        return f"[{jira_ticket}] {user_input}"
    return f"nyanyanya {user_input}"
    

if __name__ == '__main__':
    sys.exit(main())
