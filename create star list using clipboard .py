import pyperclip

emptyecheck=pyperclip.paste()
if emptyecheck!="":
    check=emptyecheck.split("\n")
    starlist=[]
    for line in check:
      starlist.append("*" + line)
       
    final='\n'.join(starlist) 
    print(final)
    
    pyperclip.copy(final)
    print(pyperclip.paste())
    pyperclip.copy("")
else:
 print("clipboard is empty") 
    