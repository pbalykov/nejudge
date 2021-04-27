import random

def kluch():
    por = hex(random.randint(10**16,10**20))[2:]
    s = ''
    for i in range(0, len(por), 4):
        k = random.randint(65,91), random.randint(65,91)
        s +=  por[i:i+2] + chr(k[0])  + por[i+2:i+4] + chr(k[1])
    
    por = ''
    k = random.randint(1, 6)
    for i in range(0, len(s), k):
        por += s[i:i+k] + chr(random.randint(65,91))

    return por
    

            
