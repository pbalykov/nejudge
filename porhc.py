a  = {0:'', 1:'0', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8' , 9:'9'}

class translt:
    
    def __new__(self,por):
        s = ''
        for i in por:
            pr = self.per_fib(i)
            pri = ''
            for i in pr:
                pri += i + '0'
            s += pri
        return self.zapol(self.spam(self.zamen(s)))

    def __init__(self):
        pass
        
   
    
    def zapol(s):
        pr = ''
        d = 0 
        for i  in range(0,len(s),4):
             
             pr +=  s[i:i + 2] + str(d) +  s[i + 2:i + 4]
             d = (d + 1) % 10

        return pr
    
    def spam(s):
        pr =  ''
        d = (65, 97) 
        for i in range(0, len(s), 5):
            
            pr  +=  '$' + s[i:i + 2] + chr(d[0]) + s[i + 2:i + 5] +  chr(d[1])
            d   = (d[0] + 1, d[1] + 1)  if d[0] != 90 else (65, 97)

        return pr

    def zamen(s):
       
       pr  = ''
       d = 0 
       for i in range(len(s)):
           if s[i] == '0':
               d += 1
               if d == 9:
                  pr += a[d]
                  d = 0 
           else:
              pr += a[d] + s[i]
              d = 0 
       return pr + a[d] 

    def per_fib(i):
       
       s1 = ord(i)
       k, k1 = 1, 1
       while k + k1 <=  s1:
             k,k1 = k1,k
             k += k1
       pr = ''
       while k1 != 0 :
          if s1 >= k:
                s1 -= k
                pr += '1'
          else:
            pr += '0'
          
          k,k1 = k1,k
          k1 -= k
       return pr







