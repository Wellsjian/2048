# 1.数据模型   编号 id  数量 number  金钱 price
# 
# 2.视图界面    显示商品信息  购买菜单  选择菜单  打印订单 找回金额
# 
# 3.逻辑控制  订单 list_order   添加商品信息   计算总价 

dict_commodity_info = {
            101: {"name": "屠龙刀", "price": 10000},
            102: {"name": "倚天剑", "price": 10000},
            103: {"name": "九阴白骨爪", "price": 8000},
            104: {"name": "九阳神功", "price": 9000},
            105: {"name": "降龙十八掌", "price": 8000},
            106: {"name": "乾坤大挪移", "price": 10000}
        }
class ShoppingModel:




    def __init__(self,aid=0,name="",price=0,count=0):
        self.aid = aid
        self.name = name
        self.price = price
        self.count = count

    @property
    def aid(self):
        return self.__aid
    @aid.setter
    def aid(self,value):
        self.__aid = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        self.__price = value

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

class ShoppingManagerController:
    def __init__(self):
        self.__list_order = []
        self.shopping_model = ShoppingModel()


    @property
    def list_order(self):
        return self.__list_order
    def add_shoping_info(self,shopping_model):

        for key in dict_commodity_info:
            if key ==  self.shopping_model.aid:
                self.__list_order.append(self.shopping_model)
        if len(self.__list_order) >0:
            return True
        return False
        

    def get_cost(self):

        cost = 0
        for item in self.__list_order:
            cost += item.price * self.shopping_model.count
        return cost

    def get_pay(self,value):
        cost = self.get_cost()
        pay = value - cost





class ShoppingView:

    def __init__(self):
        self.__controller = ShoppingManagerController()

    def shopping_info(self):

        for key, value in dict_commodity_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    def __print_shopping_info(self):

        print("""
        1)  1键购买
        2)  2键结算""")

    def __select_menu_item(self):

        number = int(input("请输入您的选择"))
        if number == 1:
            self.shopping_info()

            self.get_info()
        elif number == 2:
            shopping_model = ShoppingModel()
            for item in self.__controller.list_order:
                print("商品:%s 单价：%d 数量:%d" %(item.name,item.price,shopping_model.count))
            self.__controller.get_cost()

    def get_info(self):
        shopping_model = ShoppingModel()
        shopping_model.aid = int(input("请输入商品编号："))
        shopping_model.count = int(input("请输入购买数量："))

        self.__controller.add_shoping_info(shopping_model)



    def main(self):
        while True:
            self.__print_shopping_info()
            self.__select_menu_item()

view = ShoppingView()
view.main()




# controllor = ShoppingManagerController()
# controllor.add_shoping_info(ShoppingModel(name="屠龙刀",price = 10000))
# for item in controllor.list_order:
#     print(item.name,item.price)
