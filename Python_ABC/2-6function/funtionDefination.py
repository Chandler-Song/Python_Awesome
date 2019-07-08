# ---------- FUNCTION BASICS ----------
#
# def allotEmail(firstName, surname):
#
# 	return firstName+'.'+surname+'@pythonabc.org'
#
#
# name = input("Enter your name: ")
# fName, sName = name.split()
# compEmail = allotEmail(fName, sName)
#
# print("Your company email: \n",compEmail)



def mult_divide(num1, num2):
	return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)

