class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)
            

emp_1 = Employee('Hezzy','Buyahi',5000)
emp_2 = Employee('zzy','yahi',8000)

emp_2.fullname()
print(Employee.fullname(emp_2))