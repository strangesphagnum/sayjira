from setuptools import setup, find_packages


setup(
    name="sayjira",
    version="0.0.1",
    description="Adds a jira ticket to the beginning of a commit message",
    author="strangesphagnum",
    keywords="git commit pre-commit hook commit msg message python",
    platforms=["Any"],
    packages=find_packages(include=["sayjira"]),
    url="https://github.com/strangesphagnum/sayjira",
    install_requires=[
        "pre-commit"
    ],
    classifiers=[
        "Development Status :: Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    entry_points={
        "console_scripts": [
            "sayjira = sayjira.sayjira:main",
        ]
    }
)
