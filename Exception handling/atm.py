while True:
    balance=0
    print("ATM")
    print("""
    1)Balance
    2)Withdraw
    3)Desposite
    """)
    try:
     option=int(input("Enter the option:"))
    except Excaption as e:
        print("Error",e)
        print("Enter the 1,2 or 3 only")
        continue
        if option==1:
            print("balance $",balance)
        elif option==2:
            print("balance$",balance)
            withdraw=float(input("Enter withdraw amount:"))
            if withdraw >0:
                atmbalance=(balance-withdraw)
                print("atmbalance $",atmbalance)
            elif withdraw>balance:
                print("Your enter amount is less than balance:")
            else:
                print("Please check your balance")
        if option==3:
            print("balance $",balance)
            desposite=float(input("Enter desposite amount:"))
            if desposite>0:
                atmbalance=(balance+desposite)
                print("atmbalance $",atmbalance)
            else:
                print("some thing went worng please check")
        else:
            print("some thing went worng")