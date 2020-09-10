import os


def makedir(path):
    if os.path.exists(path):
        print(path, 'is exists')
    else:
        os.mkdir(path)
        print(path, ' has been created')


def makefile(path):
    f = open(path, 'x')
    f.close()
    print(path, ' has been created')


def ls(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        print(path, 'is not exists')


def cd(path):
    if os.path.exists(path):
        global currentpath
        currentpath = os.path.abspath(path)
        os.chdir(path)
        print('change working path to ', os.getcwd())
    else:
        print('path is not exists')


while True:
    s = input()
    if not s:
        break

    s = s.strip(' ')
    tokens = s.split(' ')
    print('parsing command >>>', tokens)
    if s.startswith('mkdir'):
        makedir(tokens[1])
    elif s.startswith('mkfile'):
        makefile(tokens[1])

    elif s.startswith('ls'):
        if (len(tokens) > 1):

            l = (ls(tokens[1]))
        else:
            l = (ls(os.getcwd()))

        for i in l:
            print(i)
    elif s.startswith('cd'):
        cd(tokens[1])
    else:
        print('Unknown command:', s)







