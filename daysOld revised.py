
#original author: William Mulbach
#I just changed this so it's easier to play with.
from datetime import datetime

from datetime import timedelta

daysOld = 42069
#You can change the daysOld value to whatever number you like.

print(str(daysOld) + ' days from today is:')

print(datetime.now() + timedelta(days=daysOld))



birthday = input("What is your birthday? YYYYMMDD \n")



#print('You will be 22000 days old on:')

#print (birthday + timedelta(days=22000))

year=int(birthday[0:4])

month=int(birthday[4:6])

day=int(birthday[6:8])

print("Your birthday is "+str(year)+"/"+str(month)+"/"+str(day)+"?")

#Maybe use an until loop here

if input("(Y/n)") in ("Y","y","",None):

    print(datetime(year,month,day)+timedelta(days=daysOld))
