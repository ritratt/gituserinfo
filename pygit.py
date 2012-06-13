from github import Github
import getpass

username = raw_input("Enter username: ")
password = getpass.getpass("Enter password: ")
g = Github(username,password)
print 'Here goes some general information for '+username
print 'Bio: '
print g.get_user().bio
print 'Blog:'
print g.get_user().blog
print 'Company:'
print g.get_user().company
print 'Name:'
print g.get_user().name
print 'URL:'
print g.get_user().url
print 'Repositories and their corresponding information will now follow:'
for repo in g.get_user().get_repos():  
  print repo.name
  commit_q=raw_input("Do you want to see the commits for this repo? Enter y for yes; anything else for otherwise. ")
  if(commit_q=='y'):
      for commit in repo.get_commits():
	print commit.sha
   
   