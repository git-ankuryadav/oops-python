import datetime
class Employee:

    raiseAmt = 1.08
    numEmp = 0
    instances = []

    def __init__(self,first,last,pay=30000):
        self.first = first
        self.last = last
        self.pay = pay 
        Employee.numEmp+=1
        Employee.instances.append(self)

    def details(self):
        print("Full name: ", self.first, self.last)

    def __str__(self):
        return "{} {}, pay: {}".format(self.first, self.last,self.pay)
    
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    
    def __len__(self):
        return len(self.first) + len(self.last)
    
    def applyRaise(self):
        self.pay = (int) (self.pay * self.raiseAmt) #for this class only - raiseAmt

    @property
    def email(self):
        return "{}.{}@company.in".format(self.first,self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @classmethod
    def raise_amt(cls, amt):
        cls.raiseAmt = amt

    @classmethod
    def fromStr(cls,stri):
        first, last, pay = stri.split("-")
        return cls(first, last,pay)
    
    @classmethod
    def printInstances(cls):
        for ins in cls.instances:
            print(ins)

    @staticmethod
    def isWeekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

class Developer(Employee):
    def __init__(self,first,last,pay,progLang):
        super().__init__(first,last,pay)
        self.progLang = progLang

    def __str__(self):
        return ((super().__str__())+(", ")+("Language: {}".format(self.progLang)))
    
class Manager(Employee):
    def __init__(self,first,last,pay,emps=None):
        super().__init__(first,last,pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def __str__(self):
        empStr = "".join(str(emp) for emp in self.emps)
        return (super().__str__()+", Employees managed: "+"{}".format(empStr))
    
    def addEmp(self, obj):
        self.emps.append(obj)
    def removeEmp(self,obj):
        self.emps.remove(obj)
 
emp1 = Employee("main","yadav")
emp2 = Employee("test","surname")

print(emp1)
print(emp2)
emp1.details()

print(emp1.pay)
emp1.applyRaise()
print(emp1.pay)

# print(Employee.__dict__)
print(Employee.raiseAmt)
print(emp1.raiseAmt)

Employee.raise_amt(1.10)

print(Employee.raiseAmt)
print(emp1.raiseAmt)
new_emps = {}


strArr = ["Adbul-Faqir-10000","Chintu-Sharma-20000","Firaq-Pandit-40000"]
for stri in strArr:
    Employee.fromStr(stri)

print(Employee.numEmp)
# print(*Employee.instances)
Employee.printInstances()

myDay = datetime.date(2025,9,14)
print(Employee.isWeekday(myDay))

# print(help(Developer))
#press 'q' to exit.

dev1 = Developer("Chinu","Bobas",70000,"Rust")
print(dev1)

mgr1 = Manager("Tinnu", "Ram", 69000, [dev1,emp1])
mgr1.removeEmp(emp1)
print(mgr1)

print(isinstance(mgr1,Employee))
print(issubclass(Manager,Developer))

print(repr(emp1))
emp13 = Employee('main','yadav',32400)
print(str(emp13))
print(Employee.numEmp)
print(len(emp13))

emp14 = Employee('ramu', 'singh', 2000)
emp14.fullname = "ramiya kumari"        #sets first and last name again just from the full name
print(emp14.email)                      #without parentheses because of @property
