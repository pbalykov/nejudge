import hashlib

def encoding_password(password:str, salt:str = None, step:int = 3)->str:
    if ( not(salt) ) :
        return hashlib.md5(password.encode("utf-8")).hexdigest()
    new_password = ''
    for i in range(0, len(password), step):
        new_password += password[i : i + step] + salt
    return hashlib.md5(new_password.encode("utf-8")).hexdigest()       
