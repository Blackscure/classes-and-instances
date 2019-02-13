class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee('Hezzy','Buyahi',5000)
emp_2 = Employee('zzy','yahi',8000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))