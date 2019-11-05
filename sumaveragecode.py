#Calculates sum and average of user-input numbers
n=[] #Initializes and empty list
sum=0 #Initializes sum to 0
avg=0 #Initializes average to 0
count=0 #count keeps track of how many numbers are inputted by the user
for x in range (0,20): #Allows for 20 user inputs
  n=input("Enter a number:")
  n=int(n) #Makes 'n' an integer so you can add to sum
  sum=sum+n #calculates sum
  count=count+1
  print()
print("Sum of 20 numbers=",sum)
avg=sum/count
print("Average is=", avg)
  
