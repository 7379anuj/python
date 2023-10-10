# # duplicate print in list 
# # l1=[2,4,2,5,4,7,1]
# # l2=[]
# # for i in l1:
# #     if i not in   l2:
# #         l2.append(i)
# #     else:
# #         print(i)
# l1=[1,7,1,7,2,5,3]
# my_dict=dict()
# count=[]

# for i in l1:
#     my_dict[i]=0
# for item in l1:
#     for key,value in my_dict.items():
#         if item==key:
#             my_dict[key]=value+1
#         j=0
# for key,value in my_dict.items():
#     if value>1:
#         print(key)


while True:
    balance=50
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
