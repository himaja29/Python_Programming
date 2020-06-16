class Employee :
    empCount = 0
    salarySum = 0

    def __init__(self, name, family, salary, Department):
        self.name = name
        self.family = family
        self.salary = salary
        self.Department = Department
        Employee.empCount += 1
        Employee.salarySum += salary

    def display_emp_count(self):
        print("total number of employees", Employee.empCount)

    def averagesalary(self):
         average = float(Employee.salarySum)/float(Employee.empCount)
         print("The Average Salary of the Employees is: ", average)

    def displayEmployee(self):
        print("Name:", self.name, "Family:", self.family, "salary:", self.salary, "Department:", self.Department)

    def demo_func(self):
        print('calling member function of parent')


class Full_time_employee(Employee):
    def __init__(self):
        print('this is the subclass: Full time employee')


if __name__=="__main__"  :
    emp1 = Employee('Himaja', 'A', 6000, 'D1')
    Employee('Yamini', "B", 7000, "D2")
    Employee('deepika', 'C', 8000, 'D3')
    Employee('manaswini', 'D', 10000, 'D4')
    Employee.averagesalary(Employee)
    e = Full_time_employee()
    e.display_emp_count()
    e.averagesalary()
    e.demo_func()
    emp1.demo_func()