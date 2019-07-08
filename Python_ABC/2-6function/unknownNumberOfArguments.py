# ---------- UNKNOWN NUMBER OF ARGUMENTS ----------
# We can receive an unknown number of arguments using
# the splat (*) operator

def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


print("Sum :", sumAll(1, 2, 3, 4))