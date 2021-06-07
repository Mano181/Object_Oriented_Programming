class employee:
    __count=0   #(__)is used for data abstraction
    def __init__(self,id,name): #constructor,self is used to tell the instance value of variable
        self.id=id
        self.name=name
        employee.__count = employee.__count+1
    company="Boomi" #default constructor

    def display(self):
        print("id: %d\nname: %s\nCompany: %s "%(self.id,self.name,self.company))

    def empcount(self):
           print("The number of employees",employee.__count)

class software: 
    def display_salary(self):  #method overriding
        print("Salary:10000")

class hardware(software): #inheritance class <new class_name>(Inherited class name)
    def display_salary(self):   #method overriding
        print("Salary:5000")   

employee_name=input("Enter the employee name: ")
emp1=employee(1,employee_name)
emp2=employee(2,"Mohan")
emp3=software()
emp4=hardware()
emp1.display()
emp4.display_salary()
emp2.display()
emp3.display_salary()
emp1.empcount()

