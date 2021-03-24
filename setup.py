from setuptools import setup, find_packages


setup(
    name="say-jira",
    version="0.0.1",
    description="Adds a jira ticket to the beginning of a commit message",
    author="strangesphagnum",
    keywords="git commit pre-commit hook commit msg message python",
    platforms=["Any"],
    # packages=find_packages(include=["say-jira"]),
    url="https://github.com/strangesphagnum/say-jira",
    # install_requires=[
    #     "pre-commit"
    # ],
    classifiers=[
        "Development Status :: In Development",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
    entry_points={
        "console_scripts": [
            "say-jira = say-jira.say-jira:main",
        ]
    }
)
