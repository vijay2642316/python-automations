import subprocess,os,shutil,time

def main():
    choices = 'clone, commit, branch, pull, fetch, merge, reset, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def clone():
    print("\nYou will be asked for the user first and then the repository name.\n")

    
    url=input("url: ")
    __url__=f'{url}'
    
    branch= input ("Branch name:")
    __branch__ =f'{branch}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    os.chdir(local_path)
    run('clone',__url__,'-b',__branch__)
    time.sleep(1)
    src=input("Type the folder path where IKP folder resides:")
    __src__=f'{src}'
    dest=input("Type the destination where u wnat to paste the IKP folder")
    __dest__=f'{dest}'
    shutil.copytree(__src__,__dest__)
    print("IKP folder copied successfully to the local git repository")
    
def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")

def branch():
    branch = input("\nType in the name of the branch you want to make: ")
    br = f'{branch}'

    run("checkout", "-b", br)

    choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y or Y":
        run("push", "-u", "origin", br)

    elif choice == "n or N":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


    src=input("\nType in the name of the branch you want to make: ")
    __src__=f'{src}'
    __dest__= clone.localpath()
    shutil.copytree(__src__,__dest__)

if __name__ == '__main__':
    main()
