# Overview
Copy one repository to another replacing with a new git user name.(using global user configuration)

## Changing git user configuration
Refer this [link](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).
```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
Replace `John Doe` and `johndoe@example.com` with your github connected account name and email.

# Requirement
* git
* python 3.6+

# Usage

1. Select a repository from your local drive or clone one from github, bitbucket or gitlab.
2. Configure git user settings.
3. Run the following command.

```bash
py main.py </path/to/original-repository> </path/to/new-repository?
```

Example:
```bash
py main.py e:/git_repository/auto-mart-original e:/git_repository/auto-mart
```
