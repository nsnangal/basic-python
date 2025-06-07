import hashlib,os,bcrypt
def check_password(password):
    #password = "innocent12@".encode()
    #hashed_password = bcrypt.hashpw(password,bcrypt.gensalt())
    #file=open("password.txt","w")
    #file.write(hashed_password)
    #file.close()
    file=open("password.txt","r")
    hashed_password=file.read()
    file.close()
    if hashed_password==password:
        return True
    else:
        return False
    
