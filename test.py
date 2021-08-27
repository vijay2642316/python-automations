import subprocess,os,shutil,time
def run(*args):
    return subprocess.check_call(['git'] + list(args))

def clone():
    print("\nYou will be asked for the user first and then the repository name.\n")

    
    url=input("url: ")
    __url__=f'{url}'
    
    branch= input ("Branch name:")
    __branch__ =f'{branch}'

    print("\nChoose the local path for your clone.")
    #local = input("Local path: ")
    local_path = r'/home/vijay/Desktop/migration/'

    os.chdir(local_path)
    run('clone',__url__,'-b',__branch__)
    time.sleep(1)
    src=input("Type the folder path where IKP folder resides:")
    __src__=f'{src}'
    __dest__="/home/vijay/Desktop/migration/IKP"   
    shutil.copytree(__src__,__dest__)
    print("IKP folder copied successfully to the local git repository")
    os.chdir('home/vijay/Desktop/migration/javaa-project')
    os.system('mvn clean install')

clone()