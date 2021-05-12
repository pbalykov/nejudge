import os

def rm(name):
    try:
        for i in os.listdir(name):
            rm(name + '/' + i)
        os.rmdir(name)
    except:
        os.remove(name)

