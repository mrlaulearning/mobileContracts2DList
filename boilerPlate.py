from operator import itemgetter
from datetime import datetime
from datetime import timedelta

contractLength=input("How many months is the contract:\n")
if contractLength == "12":
    price=29.99
elif contractLength == "24":
    price=19.99
elif contractLength == "36:
    price=9.99
else:
    print(error)


startDate=datetime.now()
monthToWeeks=contractLength//12*52
endDate=startDate+timedelta(weeks=monthToWeeks)

firstname=input("What is the client's first name:\n")
lastname=input("What is the client's last name:\n")



nameSort=sorted(names, key=lambda name: name[1])

nameSort2=sorted(names, key=itemgetter(1),reverse=True)

print(names)
print(nameSort)
print(nameSort2)
