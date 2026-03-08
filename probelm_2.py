marks1=int(input("enter the number of 1:"))
marks2=int(input("enter the number of 2:"))
marks3=int(input("enter the number of 3:"))
marks4=int(input("enter the number of 4:"))
 
 #cheching for total percentage
total_percentage =(marks1 + marks2 + marks3 +marks4)/400*100

if(total_percentage>=40):
      print("you are passed",total_percentage)
  
else: print("better luck next time")