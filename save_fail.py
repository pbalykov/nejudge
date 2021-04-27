import os

def save(pyt, fail):
    
    if not(os.path.exists(pyt + fail)):

         os.mkdir(pyt + fail)
    
    return None 

        
