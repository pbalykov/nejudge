import os, base64, obr

def rect(text):
    return text[::-1]



def decod(text):#раскадировка пути
    return ''.join(list(map(rect, base64.b64decode(text.encode()).decode().split('&'))))


def prov_put_zad(self):
    self = self[1:].split('/')
    if self[0] !=  'zadac':
        
        return False, None

    self[0] = 'zad'
    for i in range(1, len(self) - 1):
        
        self[i] = decod(self[i])
    self = '/'.join(self)

    try:
        d = os.listdir(obr.pyti(__file__) + self)
        for i in d:
            if i[-5:] == '.html':
                return True, self
        
        return False, None

    except:return False, None
        




def nach_put(self):
    s = ''
    for i in range(0,len(self), 2):

        s += rect(self[i:i+2]) + '&'

    return base64.b64encode(s[:len(s) - 1].encode()).decode()




def post_swap_get(self, metd):
    return '/' + metd + self[6:]


def in_get(self):
    self = list(self[1:].split('/'))
    if self[0] != 'testk':
   
        return False, None
    self[0] = 'tst'
    for i in range(1, len(self)-1):
        self[i] = decod(self[i])
    try:
        s = os.listdir(obr.pyti(__file__) + '/'.join(self))

        if (len(str(len(s)//2 )) - 1) * '0' + '1.txt' in s:
                return True, '/'.join(self)
        return False, None
 
    except:

        return False, None




