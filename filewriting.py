#Import the operator and datetime modules with required classes
from operator import itemgetter
from datetime import datetime
from datetime import timedelta
def main():

    #Signing up new customers
    def contractSelector():
        price=0
        #price based on contract length
        contractLength=int(input("How many months is the contract:\n"))
        if contractLength == 12:
            price=29.99
        elif contractLength == 24:
            price=19.99
        elif contractLength == 36:
            price=9.99
        else:
            #if they enter an invalid month, loop them back to the start of this function
            print("error, please select 12, 24 or 36 months")
            return contractSelector()
        print("The price for this contract is",price)


        startDate=datetime.now()
        monthToDays=contractLength//12*365
        #calculate the end date for the contract based on the timedelta class
        endDate=startDate+timedelta(days=monthToDays)
        #print(startDate)
        #print(endDate)

        #Take their details
        firstname=input("What is the client's first name:\n")
        lastname=input("What is the client's last name:\n")

        #Write to a list and then return this so it can be used by the fileWrite procedure
        custToWrite=[]
        custToWrite.append(firstname)
        custToWrite.append(lastname)
        custToWrite.append(startDate.strftime("%d/%m/%y"))
        custToWrite.append(endDate.strftime("%d/%m/%y"))
        custToWrite.append(price)
        return custToWrite

    #Take the custToWrite list as an arguement
    def fileWrite(custDetails):
        file=open("customers.txt","r")
        #read the file and evaluate the list in the file
        tempList=eval(file.read())
        file.close()

        #append the new customer's details to the list then write the list back to the file
        tempList.append(custDetails)

        customer=open("customers.txt","w")
        customer.write(str(tempList))
        customer.close()

    #printing out all customers
    def fileRead():
        customerOut=open("customers.txt","r")
        custList=eval(customerOut.read())
        customerOut.close()
        pad=" "
        print("All customers")
        for count in range(len(custList)):
            for details in range(len(custList[0])):
                print(str(custList[count][details])+pad*(12-len(str(custList[count][details]))),end="")
            print()

        #two different ways of sorting the list by surname or (descending price)

        #using a lambda function
        nameSort=sorted(custList, key=lambda name: name[1])

        print("\nSorted by surname, unformatted:")

        for counter in range(len(nameSort)):
            print(nameSort[counter])
            
        #using the itemgetter class
        nameSort2=sorted(custList, key=itemgetter(4),reverse=True)

        print("\nSorted by price (descending), unformatted:")
        
        for names in range(len(nameSort2)):
            print(nameSort2[names])    
        
    task=input("What do you want to do? \n\
A) Add a new customer contract \n\
B) Output all existing customers\n").upper()

    if task == "A":
        custDetails=contractSelector()
        fileWrite(custDetails)
    else:
        fileRead()
    main()


        

        
    

main()





