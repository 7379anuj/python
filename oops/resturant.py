class Restaurant ():
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
print(add_items)
print(book_table_)