from setuptools import setup, find_packages


setup(
    name="sayjira",
    version="0.1.0",
    description="Adds a jira ticket from branch name to the beginning of a commit message",
    author="strangesphagnum",
    keywords="git commit pre-commit hook commit msg message python",
    platforms=["Any"],
    packages=find_packages(include=["sayjira"]),
    url="https://github.com/strangesphagnum/sayjira",
    install_requires=[
        "pre-commit",
        "GitPython"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    entry_points={
        "console_scripts": [
            "sayjira = sayjira.sayjira:main",
        ]
    }
)
