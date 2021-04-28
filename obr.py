def pyti(self):# обрез пути
    while self[len(self) - 1:]  != '/' and len(self) != 0:
        self = self[:len(self) - 1]
    return self 

def reg(self):# обрез последнего символа
    if self[-1:] == '&':
        return self[: - 1]
    return self



def fail_leng(self):# красивый деление делит где код а где язык а где колд
    self = list(self.split(b'\n'))
    lang = self[3][:len(self[3])-1]
    text = b''
    for i in range(8,len(self) - 3):
        text += self[i] + b'\n' 
    return  lang.decode('utf-8'), text.decode('utf-8')




def check(line, param):
     for i in line.lower():
        if  not('a' <= i  <= 'z')  and  not('0' <= i <= '9') and not(i in param):
            return True
     return False





def regist(self):
    if self[2] != self[3] or len(self[2]) < 6 or len(self[1]) < 3:
        return False
    
    if check(self[1], ('-', '_', '$')):return False
    if check(self[2], ('-', '_', '$', '#', "!", "?", ".", ";")):return False

    s = 0 
    for i in self[0].lower():# Имя пользавателя
        if i in (' ', '\t'):
            s += 1
        if not('а' <= i <= 'я') and not('a' <= i  <= 'z') and not(i in('\t', ' ')) and  s < 2: 
            return False

    return True if len(self[0]) - s > 3 else False
    

    
