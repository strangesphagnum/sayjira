# Description
A ridiculously simple pre-commit hook that parses and adds jira ticket from git branch to your commit messages.

Template: **[BEEP-666] your commit message**

# Pre-commit setup
To be used with [pre-commit](https://pre-commit.com/) package manager installed.

### Enter command in command line
```
pre-commit install --hook-type pre-commit --hook-type prepare-commit-msg
```

If you need to overwrite hooks pass: 
```
pre-commit install --hook-type pre-commit --hook-type prepare-commit-msg --overwrite
```

### Provide repo inside pre-commit-config.yaml
Provide one of the [available versions](https://pypi.org/project/sayjira/).
```
repos:
  - repo: https://github.com/strangesphagnum/sayjira
    rev: 0.1.2
    hooks:
      - id: sayjira
```

### Note
If you provide stage to all your hooks like:
```
repos:
  - repo: https://github.com/strangesphagnum/sayjira
    rev: 0.1.2
    hooks:
      - id: sayjira
      - stages: [prepare-commit-msg]
```
Pre-commit won't run hooks twice

That's it. Enjoy!