import os
import yaml

def init(rootFolder):
    choice = input("mode?\n[1]SSH\n[2]rdp\n[3]exit\n[4]open folder\nchoice==> ")
    print(choice)

    match choice:
        case '1':
            print('ssh')
            listHosts(rootFolder + '\ssh.yaml','ssh')
        case '2':
            print('rdp')
            listHosts(rootFolder + '\\rdp.yaml','rdp')
        case '3':
            print('exit')
            exit(0)
        case '4':
            print('opening folder')
            os.system('explorer.exe '+rootFolder)
            exit(0)
        case _:
            print('pendejo')
            exit(1)

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
        #for item in sshLoaded:
           #print(item.['ip'])

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