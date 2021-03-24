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


def main():
    branch_name = get_branch_name()
    jira_ticket = get_jira_ticket(branch_name)
    return jira_ticket
    

if __name__ == '__main__':
    main()