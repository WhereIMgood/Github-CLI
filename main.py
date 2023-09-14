import requests
import colorama
import os
import sys

colorama.init()
repos_ = []
def list_repos(username):
    token = "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"

    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    repos = response.json()

    for repo in repos:
        git_url = repo["git_url"].replace("git://", "https://")
        name = repo["name"]
        repos_.append(git_url)
        print(colorama.Fore.GREEN + name, colorama.Fore.YELLOW + " -------- ",
              colorama.Fore.BLUE + git_url)


print(colorama.Fore.WHITE)

def download_menu():
	count = 0
	print(colorama.Fore.YELLOW+f"Which repo you want to clone?")
	for repo in repos_:
		count += 1
		print(colorama.Fore.WHITE+f" {count}- {repo}")
	print(colorama.Fore.YELLOW+"type ('exit' or 'quit') to Quit the program")
	choice = input(colorama.Fore.WHITE+"Enter repo number: ")
	if choice == "exit" or choice == "quit":
		sys.exit()
	else:
		choice_ = int(choice) - 1
		repo_ = repos_[choice_]
		print(colorama.Fore.WHITE+f"Cloning {repo_}...")
		os.system(f'git clone {repo_}')
		print(colorama.Fore.YELLOW+"\nRepo Cloned")


def search(repo):
	pass

def main():
	print("Welcome to github CLI\n Here you can list all the repos of a user and you can also clone them\nNote: You have to install git before you run the script.")
	username_ = input("Enter a github username: ")
	list_repos(username_)
	while True:
		download_menu()

if __name__ == "__main__":
	main()