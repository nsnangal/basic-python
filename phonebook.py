from collections import defaultdict
import pprint,os
phonebook=defaultdict(list)
def add():
  while True:

     name=input("Enter your name\n")
     check=name
     if check.replace(" ","").isalpha()==False:
       print("please enter characters only: ")
     elif check.replace(" ","").isalpha():
        break 

      
  while True:

      ph_no=input("Enter your phone number\n")
      if ph_no.strip().isdigit()==False:
       print("please enter numbers only only:")
      elif ph_no.strip().isdigit()==True:
         break

  phonebook['name'].append(name)
  phonebook['phone_no'].append(ph_no)
  os.system("cls")  
  print("Record insered successfully\n")
def update(up_dic):
    print("what would you like to update press 1. name \n 2. contact \n 3. Both")
    updatetype=int(input())
    
    if updatetype>3 and updatetype<0:
      print("Enter accurate number:\n")
      update(up_dic)

    name=input("enter existing name to fetch your record : \n")
    
    for value in up_dic.values():
            
      if name in value and updatetype==1:
       index=value.index(name)
       newname=input("enter new name :")
       up_dic["name"][index]=newname
       os.system("cls")
       print("name modified sucessfully")
       break
      elif name in value and updatetype==2:
       index=value.index(name)
       newname=input("enter new phone number :")
       up_dic["phone_no"][index]=newname
       os.system("cls")
       print("phone number modified sucessfully")
       break
      elif name in value and updatetype==3:
       index=value.index(name)
       newname=input("enter new name : \n")
       newphone=input("enter new phone number : \n")
       up_dic["name"][index]=newname
       up_dic["phone_no"][index]=newphone
       os.system("cls")
       break
      else:
       os.system("cls")
       print("Record doesnot exist.") 
       
       break
    
def delete(del_dic):
  name=input("enter name which data you want to delete\n")
  for value in del_dic.values():
    if name in value:
      index=value.index(name)
      del del_dic["name"][index]
      del del_dic["phone_no"][index]
      os.system("cls")
def display(show_dic):
    os.system("cls")
    name=show_dic["name"]
    phone_no=show_dic["phone_no"]
    
    for length in range(len(name)):
      print(f"({length +1})  {name[length]}   :  {phone_no[length]}")

while True:
  
  print("Press respective number to perform operation :-\n  1. To add in the phonebook.\n 2. To Update existing contact. \n 3. To Display all records. \n "
  "4. To Delete existing contact. \n 5. To Exit.")
  check=input()
  os.system("cls")
  if check.strip()=="1":
    add()
  elif check.strip()=="2":
    update(phonebook)
  elif check.strip()=="5":
    break
  elif check.strip()=="4":
    delete(phonebook)
  elif check.strip()=="3":
    display(phonebook)


