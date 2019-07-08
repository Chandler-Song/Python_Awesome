# class Employee(object):
# 	pass
#
# employee1 = Employee()
# employee1.first = 'Harry'
# employee1.surname = 'Potter'
# employee1.salary = 4000
# employee1.email = 'Harry.Potter@PythonABC.com'
# print('{}, {}, {}'.format(employee1.first + ' ' +employee1.surname,
# 						  employee1.salary, employee1.email))
#
# employee2 = Employee()
# employee2.first = 'Bilbo'
# employee2.surname = 'Baggins'
# employee2.salary = 6000
# employee2.email = 'Bilbo.Baggins@PythonABC.com'
# print('{}, {}, {}'.format(employee2.first + ' ' +employee2.surname,
# 						  employee2.salary, employee2.email))

class Employee():

	raiseAmount = 1.04
	employeeNum = 0

	def __init__(self, first, surname, salary):
		self.first = first
		self.surname = surname
		self.salary = salary
		self.email = first + '.' + surname + '@PythonABC.com'

		Employee.employeeNum += 1

	def infoSummary(self):
		return '{}, {}, {}'.format(self.first + ' ' + self.surname,
						  self.salary, self.email)

	def raiseSalary(self):
		self.salary = self.salary * self.raiseAmount

employee1 = Employee('Harry', 'Potter', 4000)
employee2 = Employee('Bilbo', 'Baggins', 6000)
employee3 = Employee('Mark', 'Twain', 8000)
employee4 = Employee('Julius', 'Caesar', 12000)


print(employee2.infoSummary())
employee2.raiseAmount = 1.08
employee2.raiseSalary()
print(employee2.infoSummary())

# print(employee2.__dict__)
# print(employee1.__dict__)
# print(employee1.raiseAmount)
# print(Employee.__dict__)

print('there is {} employees'.format(Employee.employeeNum))




