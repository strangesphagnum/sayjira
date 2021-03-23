from pathlib import Path


def branch_name():
    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as git:
        content = git.read().splitlines()
        for line in content:
            if "ref:" in line:
                return line.split("/")[-1]


print(get_active_branch_name())
