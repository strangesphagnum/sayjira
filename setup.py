from setuptools import setup


setup(
    name="say-jira",
    version="0.0.1",
    description="Adds a jira ticket to the beginning of a commit message",
    author="strangesphagnum",
    keywords="git commit pre-commit hook commit msg message python",
    platforms=["Any"],
    packages=["say-jira"],
    scripts=["say-jira"],
    install_requires=[
    ],
    classifiers=[
        "Development Status :: In Development",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)
