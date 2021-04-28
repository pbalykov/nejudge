import subprocess, os, ctypes


def obr(pr, tv, arr): 
    if pr == tv:
        return True
    try:
        pr = int(pr[0]) - 1, int(pr[1]) - 1
        tv = int(tv[0]) - 1, int(tv[1]) - 1
        if  len(tv) > 2 or not(-1 < tv[0] < tv[1]) or tv[0] - tv[1] !=  pr[0] - pr[1]: return False
        i = tv[0]
        while arr[i] <= arr[i+1] and i != tv[1] + 1  :
            
            i += 1

        if i + 1 == tv[1]   :
            
            return True
        
        return False

    except:
        return False







lang_komp = {'.c':"gcc",
          '.cpp':"g++",
          '.rs':"rustc",
          '.pas':"fpc"}


def pes(folder, test, nam_pos, lang):
    a = []
    komp = False
    if lang in lang_komp:
             s = [lang_komp[lang], folder + '/' + str(nam_pos) + lang]
             if lang  in ('.c', '.cpp'): s +=   ['-o', folder + '/' +  str(nam_pos)]
           
             p = subprocess.Popen(s, stderr = open(folder + '/err.txt', 'wb'), stdout = open(folder + '/otv.txt', 'wb'))
             try: 
                p.wait(1)

             except: 
                  
                 p.kill()
                 return [0] * 50
                
             if  str(nam_pos) not in os.listdir(folder) :
                 return [0] * 50 

             komp  = True
    
    s = len(os.listdir(test)) // 2
    for i in range(s ):
        i = (len(str(s)) - len(str(i + 1))) * '0' + str(i + 1) 
        if not(komp):
            p = subprocess.Popen(['python3', folder + '/' + str(nam_pos) + lang], stdin = open(test + '/' + i + '.txt', 'rb'), stdout = open(folder + '/otv.txt', 'wb'), stderr = open(folder + '/err.txt', 'wb'))
            try: 
                p.wait(1)
            except: 
                p.kill()
                a.append(0)
                continue

        else:
            p = subprocess.Popen([folder + '/' + str(nam_pos)], stdin = open(test + '/' + i + '.txt', 'rb'), stdout = open(folder + '/otv.txt', 'wb'), stderr = open(folder + '/err.txt', 'wb'))
            try: 
                p.wait(1)
            except: 
                p.kill()
                a.append(0)
                continue

    

        if open(folder + '/err.txt', 'r').read() != '':
           a.append(3)
 
        elif obr(open(test + '/' + i + 'a.txt', 'r').read()[:-1].split('\n'), open(folder +'/otv.txt', 'r').read()[:-1].split(' '),  list(map(int, open(test + '/' + i + '.txt', 'r').read()[:-1].split('\n')[1:]))):
            a.append(1)
        else:
            a.append(0)
    return a
    

      
