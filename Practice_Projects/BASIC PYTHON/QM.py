# create questions for quizes based on country,states and their capital.
import os,world_capitals,random
question=[]
countrylist=[]
stateslist=[]
storeanswer=[]

def makequestions():
 for country,states in world_capitals.capitals.items():
    
    question.append(f'What is the name of Capital of "{country}"?')
    countrylist.append(country)
    for state in states.keys():
        if "Capital" in state:
           countrylist.append(states[state])
           
        else:
         for keys in world_capitals.capitals[country]["States"]:
          question.append(f'What is the name of Capital of "{keys}"?')
          stateslist.append(keys)
          stateslist.append(world_capitals.capitals[country]["States"][keys])
          
#randomize questions with options
def create_quiz():
 
 for quizno in range(36):
      
      print("quiz numder :", quizno+1)
      randomquestion=random.sample(range(1,50),35)
      quesno=0
      quizfile=open("quizfile%s.txt" % (quizno+1),"w")
      quizfile.write("QUIZ NUMBER: %d \n NAME: \n  Subject: \n" % (quizno+1))
                 
      correctanswer=[]
      for num in randomquestion:                           #create 35 random questions
        quesno+=1    
        check=question[num]       
        print(f"Q:{quesno}",check)
        newcheck=check.split('"')
        quizfile.write(f"Q:{quesno} {question[num]} \n")
        cost=newcheck[1]
                           
        if cost in countrylist:
             indexcountry=countrylist.index(cost)
             indexcountry=indexcountry+1
             optioncountry=[]
             optioncountry.append(countrylist[indexcountry])
             countryanswer=countrylist.copy()
             correctanswer.append(countryanswer[indexcountry])
             
             flagcountryindex=random.sample(range(1,5),3)
             for index in flagcountryindex:
               optioncountry.append(countrylist[index])
             random.shuffle(optioncountry)  
             for indexprint in range(4):   
               print(f"({indexprint+1}) {optioncountry[indexprint]}")
               quizfile.write( f"({indexprint+1}) {optioncountry[indexprint]}\n")           
               
              
             storeanswer.append(optioncountry.index(correctanswer[0])+1)    
             correctanswer=[]     
             cost=""

        elif cost in stateslist:
             indexstates=stateslist.index(cost)
             indexstates=indexstates+1
             optionstates=[]
             optionstates.append(stateslist[indexstates])
             stateanswer=stateslist.copy()
             correctanswer.append(stateanswer[indexstates])
             flagstateindex=random.sample(range(1,20),3)
             for index1 in flagstateindex:
               optionstates.append(stateslist[index1])
             random.shuffle(optionstates)  
             for indexprint in range(4):   
               print(f"({indexprint+1}) {optionstates[indexprint]}")
               quizfile.write( f"({indexprint+1}) {optionstates[indexprint]}\n")
               
              
             storeanswer.append(optionstates.index(correctanswer[0])+1)    
             correctanswer=[]                                    
             cost=""
      for printanswer in range(len(storeanswer)):       
        quizfile.write(f" Q({printanswer+1}):{storeanswer[printanswer]}")      
      quizfile.close()     

makequestions()
create_quiz()                        
      


                  


    



