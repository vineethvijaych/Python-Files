import transaction_module as t
print("login with name and account number")
n=input("enter name:")
ac=int(input("enter a/c number:"))
if n==t.v.n1 and ac==t.v.ac1:
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    o=input("select an option(1,2,3):")
    if o=="1":
        t.v.balance()
        print("thank you")
        print("do you want to deposit/withdraw?")
        g=input("enter an option(yes/no):")
        if g=="yes":
            print("1.deposit")
            print("2.withdraw")
            k=input("select an option(1,2):")
            if k=="1":
                h=int(input("enter deposit amount:"))
                print("deposited succesfully")
                t.v.deposit(h)
                print("thank you")
            else:
                print("avaliable balance:",t.v.b)
                i=int(input("enter withdraw amount:"))
                print("withdrawed successfuly")
                t.v.withdraw(i)
                print("thank you")
        else:
            print("thank you")  
    elif o=="2":
        e=int(input("enter deposit amount:"))
        print("deposited succesfully")
        t.v.deposit(e)
        print("thank you")
    elif o=="3":
        print("avaliable balance:",t.v.b)
        f=int(input("enter withdraw amount:"))
        print("withdrawed successfuly")
        t.v.withdraw(f)
        print("thank you")
else:
    print("check name and a/c number again")
