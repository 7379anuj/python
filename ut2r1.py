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


class Restaurant ():
    menu_items={}
    def __init__(self):
        self.menu_items=dict()
        self.book_table=[]
        self.customer_order=[] 
    def add_items(self,item):
         self.menu_items["items"]=item
    def book_table_(self, table_number):
         self.book_table.append(table_number)
    def customer_order_(self, table_number,order): 
        order_detail={"table_number": table_number,'order':order} 
        self.customer_order.append(order_detail)
r1= Restaurant()
r1.add_items('Pizza')
r1.add_items('Tea') 
r1.add_items('samosa') 
r1.book_table_(1) 
r1.book_table_(2) 
r1.book_table_(3) 
r1.customer_order_(1,"Tea") 
r1.customer_order_(2,"samosa")
