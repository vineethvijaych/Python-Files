# Write a Python function called "safe_divide" that takes two parameters, num1 and num2. The function should divide num1 by num2 and return the result. Handle the ZeroDivisionError exception within the function and return None if the division is not possible.
try:
    class calculate:
        num1=10
        num2=0
        def safe_divide(self):
            a=self.num1/self.num2
            print(a)
    b=calculate()
    b.safe_divide()
except:
    print("ZeroDivisionError: division by zero")
else:
    print("function wrkd")
finally:
    print("program continue...")