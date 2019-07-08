# Property


class Employee(object):

	raiseAmount = 1.04
	employeeNum = 0

	def __init__(self, first='Unknown', surname='Unknown', salary=0):
		self.__first = first
		self.__surname = surname
		self.__salary = salary

		Employee.employeeNum += 1

	@property
	def email(self):
		return self.__first + '.' + self.__surname + '@PythonABC.com'

	@property
	def fullname(self):
		return self.__first + ' ' + self.__surname

	@fullname.setter
	def fullname(self, value):
		if isinstance(value, str):
			self.__first, self.__surname = value.split()

	@property
	def first(self):
		return self.__first

	@first.setter
	def first(self, value):

		if isinstance(value, str):
			self.__first = value
		else:
			print('Firstname must be string')

	@property
	def surname(self):
		return self.__surname

	@surname.setter
	def surname(self, value):

		if isinstance(value, str):
			self.__surname = value
		else:
			print('Surnamename must be string')

	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self, amount):
		if isinstance(amount, int) or isinstance(amount, float):
			self.__salary = amount
		else:
			print('Salary must be interger or float')

	def infoSummary(self):
		return '{}, {}, {}'.format(self.fullname,
						  self.salary, self.email)

	def raiseSalary(self):
		self.salary = self.salary * self.raiseAmount

	@classmethod
	def setRaiseAmount(cls, amount):
		cls.raiseAmount = amount

	@classmethod
	def newFromString(cls, empstr):
		first, surname, salary = empstr.split('-')
		return cls(first, surname, salary)

	@staticmethod
	def whatDay(day):
		num = day.weekday()
		if num == 0:
			print('\nLet\'s look at the bright side. At least Mondays only happen once a week')
		if num == 1:
			print('\nThank goodness Monday is gone. Happy Tuesday!')
		if num == 2:
			print('\nIt’s Wednesday. That means that we are over the hump!')
		if num == 3:
			print('\nHappy Thursday! P.S. It’s almost Friday!')
		if num == 4:
			print('\nHello Friday, where have you been all week?')
		if num == 5:
			print('\nSaturday is the perfect day for a wonderful adventure')
		if num == 6:
			print('\nOn this lovely Sunday...')


# class Writer(Employee):
#
# 	raiseAmount = 1.08
#
# 	def __init__(self, first, surname, salary, masterwork):
# 		Employee.__init__(self, first, surname, salary)
# 		self.masterwork = masterwork
#
# 	def infoSummary(self):
# 		return '{}, {}, \n{}, \n{}\n'.format(self.first + ' ' + self.surname,
# 						  self.salary, self.email, self.masterwork)
#
# 	@classmethod
# 	def newFromString(cls, empstr):
# 		first, surname, salary, masterwork = empstr.split('-')
# 		return cls(first, surname, salary, masterwork)
#
#
# class Leader(Employee):
#
# 	def __init__(self, first, surname, salary, employees=None):
# 		super().__init__(first, surname, salary)
# 		if employees is None:
# 			self.employees = []
# 		else:
# 			self.employees = employees
#
# 	def infoSummary(self):
#
# 		nameList = []
#
# 		for e in self.employees:
# 			nameList.append(e.first + ' ' + e.surname)
#
# 		return '{}, {}, \n{}, \n{}\n'.format(self.first + ' ' + self.surname,
# 						  self.salary, self.email, nameList)
#
# 	def addEmp(self, emp):
# 		if emp not in self.employees:
# 			self.employees.append(emp)
#
# 	def delEmp(self, emp):
# 		if emp in self.employees:
# 			self.employees.remove(emp)
#
# 	@classmethod
# 	def newFromString(cls, empstr):
# 		print('\nSorry, it does not work for Leader\n')


# empCharacter1 = Employee('Harry', 'Potter', 4000)
empCharacter1 = Employee('Harry')
empCharacter2 = Employee('Bilbo', 'Baggins', 6000)

# empWriter1 = Writer('Mark', 'Twain', 8000, 'The adventure of Tom Sawyer')
#
# empLeader = Leader('Julius', 'Caesar', 12000, [empCharacter1, empCharacter2])
#
# empStr1 = 'J.K-Rowling-10000-Harry Potter'
# empStr2 = 'J.R.R-Tolkien-8000-The lord of rings'
# empWriter2 = Writer.newFromString(empStr1)
# empWriter3 = Writer.newFromString(empStr2)

print(empCharacter1.infoSummary())

empCharacter1.surname = 'Potter'

print(empCharacter1.infoSummary())






