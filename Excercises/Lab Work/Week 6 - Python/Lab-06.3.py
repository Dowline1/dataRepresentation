from github import Github
import requests

g = Github("7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0")

#for repo in g.get_user().get_repo():
    #print(repo.name)
    #repo.edit(has_wiki=False)
    # View all attributes and methods
    #print(dir(repo))

repo = g.get_repo("datarepresentationstudent/aPrivateOne")
print(repo.clone_url)