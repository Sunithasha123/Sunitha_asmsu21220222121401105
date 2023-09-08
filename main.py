yr=int(input("Enter year"))
if(yr%400==0)and(yr%100==0):
  print("{0}is a leap year". format(yr))
elif(yr%4==0)and(yr%100!=0):
  print("{0}is a leap year". format(yr))
else:
  print("{0}is not a leap yaer". format(yr))