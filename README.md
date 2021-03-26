# Description
A ridiculously simple pre-commit hook that parses and adds jira ticket from git branch to your commit messages.

I.e: **[BEEP-666] {entered commit message}**

# Pre-commit setup
To be used with [pre-commit](https://pre-commit.com/) package manager installed.

### Enter commands in command line
```
pre-commit install
pre-commit install --hook-type prepare-commit-msg
```

### Provide repo inside pre-commit-config.yaml
Provide one of the [available versions](https://pypi.org/project/sayjira/).
```
repos:
  - repo: https://github.com/strangesphagnum/sayjira
    rev: 0.1.0
    hooks:
      - id: sayjira
```

That's it. Enjoy!