

class Employee(object):

	__slots__ = ('__first', '__surname', '__salary', 'nickname')

	raiseAmount = 1.04
	employeeNum = 0

	def __init__(self, first='Unknown', surname='Unknown', salary=0):
		self.first = first
		self.surname = surname
		self.salary = salary

		Employee.employeeNum += 1

	@property
	def email(self):
		return self.first + '.' + self.surname + '@PythonABC.com'

	@property
	def fullname(self):
		return self.first + ' ' + self.surname

	@fullname.setter
	def fullname(self, value):
		if isinstance(value, str):
			self.first, self.surname = value.split()

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
		return '\n{}, {}, {}\n'.format(self.fullname,
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

class Writer(Employee):

	raiseAmount = 1.08

	def __init__(self, first, surname, salary, masterwork=''):
		Employee.__init__(self, first, surname, salary)
		self.masterwork = masterwork

	def infoSummary(self):
		return '{}, {}, \n{}, \n{}\n'.format(self.fullname,
						  self.salary, self.email, self.masterwork)

	@classmethod
	def newFromString(cls, empstr):
		first, surname, salary, masterwork = empstr.split('-')
		return cls(first, surname, salary, masterwork)

	def __add__(self, otherWriter):
		if isinstance(otherWriter, Writer):
			return '{} and {}'.format(self.masterwork, otherWriter.masterwork)
		else:
			return 'Kindly register {}\' masterwork at first, thanks'.format(otherWriter.fullname)

class Leader(Employee):

	def __init__(self, first, surname, salary, employees=None):
		super().__init__(first, surname, salary)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def __repr__(self):
		return '\n__repr__: {}\n'.format(self.infoSummary())
	#
	def __str__(self):
		return '\n__str__: {}\n'.format(self.fullname)
	def __len__(self):
		return len(self.employees)

	def infoSummary(self):

		nameList = []

		for e in self.employees:
			nameList.append(self.fullname)

		return '{}, {}, \n{}, \n{}\n'.format(self.fullname,
						  self.salary, self.email, nameList)

	def addEmp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def delEmp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	@classmethod
	def newFromString(cls, empstr):
		print('\nSorry, it does not work for Leader\n')

class Duck(object):

	def infoSummary(self):
		return '\nIn fact, I am a duck!\n'

def annualIncreaseRate(obj):
	print('\nAnnual salary increase rate for {} is {}\n'.format(
							type(obj).__name__, obj.raiseAmount))

def output(obj):

	if hasattr(obj, 'infoSummary'):
		print(obj.infoSummary())
	else:
		print('No comment' )


empCharacter1 = Employee('Harry', 'Potter', 4000)
empCharacter2 = Employee('Bilbo', 'Baggins', 6000)

empWriter1 = Writer('Mark', 'Twain', 8000, 'The adventure of Tom Sawyer')

empLeader = Leader('Julius', 'Caesar', 12000, [empCharacter1, empCharacter2])

empStr1 = 'J.K-Rowling-10000-Harry Potter'
empStr2 = 'J.R.R-Tolkien-8000-The lord of rings'
empWriter2 = Writer.newFromString(empStr1)
empWriter3 = Writer.newFromString(empStr2)

# print(type(empLeader))
# print(type(empLeader).__name__)

# polymorphism

# annualIncreaseRate(empCharacter1)
# annualIncreaseRate(empWriter1)
# annualIncreaseRate(empLeader)

# output(empLeader)
# output(empWriter2)
# output(empCharacter1)
# # #
# output('Harry Potter')
# #
# donaldDuck = Duck()
# output(donaldDuck)

# __repr__ and __str__
# print(empLeader)
# print(empLeader.__repr__())
# print(empLeader.__str__())

# __add__
# print(1+2)
# print(int.__add__(1, 2))
# print('glory ' + 'Godness')
# print(str.__add__('joy ' , 'Godness'))
#
# print(empWriter2 + empWriter3)
# print(empWriter2 + empLeader)

# __eq__ : Equal
# __ne__ : Not Equal
# __lt__ : Less Than
# __gt__ : Greater Than
# __le__ : Less Than or Equal
# __ge__ : Greater Than or Equal
# __add__ : Addition
# __sub__ : Subtraction
# __mul__ : Multiplication
# __div__ : Division
# __mod__ : Modulus

# __len__()
# print(len('blue moon'))
# print('blue moon'.__len__())
# print(len(empLeader))

# __slot__
empCharacter1.nickname = 'Pikachu'

print(empCharacter1.nickname)














# from datetime import date
#
# a = date.today()
# b = str(a)
# print(a)
# print(b)
# print(a.__str__())
# print(b.__str__())
# print(a.__repr__())
# print(b.__repr__())







