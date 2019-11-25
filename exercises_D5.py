class Employee:
    
    def __init__(self,Number,Name,Address,Salary,JobTilte):
            self.number =int(Number)
            self.__name = Name
            self.__address = Address
            self.__salary = float(Salary)
            self.__jobTilte = JobTilte
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getSalary(self):
        return self.__salary    
    def setAddress(self,newAdd):
        self.__address=newAdd
        print (" New Address for Employee",self.number,self.__address)
    def getJobTilte(self):
        return self.__jobTilte   
    def __del__( self):
        print (self.__name,'has been deleted')
    def printHorizntal( self):
        print ("* Employee",self.number,"information :")
        print ("  * Employee Number :",self.number)
        print ("  * Name :",self.__name)
        print ("  * Address :",self.__address)
        print ("  * Salary :",self.__salary)
        print ("  * JobTilte :",self.__jobTilte ,"\n")
    def printVertical(self):
        print ("Employee",self.number,"information :",end=" ")
        print ("Employee Number :",self.number,end=" ")
        print ("Name :",self.__name,end=" ")
        print ("Address :",self.__address,end=" ")
        print ("Salary :",self.__salary,end=" ")
        print ("JobTilte :",self.__jobTilte)

Employee1= Employee(1,"mohamed Khaled","Amman jordan",500,"consultant")
Employee2= Employee(2,"Hala Rana","Aqaba jordan",500,"Manager")

Employee1.printHorizntal()
Employee2.printVertical()

Employee1.setAddress("USA")

del Employee1
del Employee2