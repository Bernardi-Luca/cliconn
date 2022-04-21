import os
import yaml

def init(rootFolder):

    print(' ██████╗██╗     ██╗ ██████╗ ██████╗ ███╗   ██╗███╗   ██╗ ')
    print('██╔════╝██║     ██║██╔════╝██╔═══██╗████╗  ██║████╗  ██║ ')
    print('██║     ██║     ██║██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║ ')
    print('██║     ██║     ██║██║     ██║   ██║██║╚██╗██║██║╚██╗██║ ')
    print('╚██████╗███████╗██║╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║ ')
    print(' ╚═════╝╚══════╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝ ')

    choice = input("mode?\n[1]SSH\n[2]rdp\n[3]exit\n[4]open conf folder\nchoice==> ")
    print(choice)

    match choice:
        case '1':
            print('--- ssh selected ---')
            listHosts(rootFolder + '\ssh.yaml','ssh')
            returnCmd()
        case '2':
            print('--- rdp selected ---')
            listHosts(rootFolder + '\\rdp.yaml','rdp')
            returnCmd()
        case '3':
            print('--- exiting ---')
            returnCmd()
        case '4':
            print('--- opening folder ---')
            os.system('explorer.exe '+rootFolder)
            returnCmd()
        case _:
            print('pendejo >:(')
            exit(1)
            returnCmd()

def listHosts(sshConf,mode):
    with open(sshConf) as sshConf:
        sshLoaded = yaml.load(sshConf, Loader=yaml.FullLoader)
        hosts = list(sshLoaded.keys())
        os.system('cls')
        for item in hosts:
            print(str(hosts.index(item)) + " - " + str(item))

        choice = input("which host? ==> ")

        item = sshLoaded.get(hosts[int(choice)])
        print(item)

    match mode:
        case 'ssh':
            print('mode ssh')
            execSSH(item)
        case 'rdp':
            print('mode rdp')
            execRDP(item)

def execSSH(itemDict):
    addr = itemDict.get('ip')

    if 'user' in itemDict:
        user = itemDict.get('user')
    else:
        user = input("which user for host" + addr +"?")

    os.system('cmd /c ssh '+user+'@'+addr)

def execRDP(itemDict):
    addr = itemDict.get('ip')

    comm = 'cmd /c mstsc /v '+addr+' /prompt'

    if 'width' in itemDict and 'height' in itemDict:
        width = itemDict.get('width')
        height = itemDict.get('height')
        comm = comm + ' /w ' + str(width) + ' /h '+str(height)
    else:
        comm = comm + ' /f'

    os.system(comm)

def returnCmd():
    os.system('cmd')
    exit(0)
