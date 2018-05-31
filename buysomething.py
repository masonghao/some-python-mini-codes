from time import strftime, sleep
class BuySomeThing():
    """
    This is a top class for buy some thing.
    It be use to my AI project.
    My AI project exists in the near future.
    I am Msong
    """
    def __init__(self, thingName, budget):
        self.thing = thingName # 要购买的东西
        self.mallList=[] # 要购买的东西的商店列表
        self.discount = 1 # 要购买的东西默认折扣无（打十折）
        self.toBuy = False # 默认不买了
        self.budget = budget # 预算
        self.createTime = strftime("%Y-%m-%d %H:%M:%S")
        self.selectName = None
        self.selectDis = None
        self.selectNum = None
        self.selectPrice = None
        self.getMallList()
        self.compare()

    def compare(self):
        for x in self.mallList:
            if self.selectDis:
                if self.selectDis > float(x['discount']):
                    self.doBuy(x)
            else:
                self.doBuy(x)

    def doBuy(self, company):
        discount = float(company['discount'])
        self.selectDis = discount
        if discount < 1:
            self.selectName = company['company']
            self.selectPrice = float(company['price'][1:])
            if discount < 0.5:
                self.selectNum = 2
            else:
                self.selectNum = 1 
        else:
            self.selectName = company['company']

    # 抓取相关数据
    def getMallList(self):
        mallList = GetMallApi
        self.mallList = mallList.get(1)

    def showrResult(self):
        print('购买'+self.thing+'可以去 '+self.selectName, end=' ')
        print('购置数量 '+str(self.selectNum), end=' ')
        print('单价 '+str(self.selectPrice)+'打 '+str(10*self.selectDis)+' 折', end=' ')
        print('花费 '+str(self.selectPrice*self.selectDis*self.selectNum))

if __name__ == '__main__':
    '''
    假如要买一架飞机：
    1.去哪儿买？ 2.是否打折 3.是否五折以下 4.买1/2架
    5.去下一个商店看看（是否有下一家） 6.不买了
    '''
    # 一个假的接口，use to get some info
    class GetMallApi:
        def __init__(self):
            pass
        def get(self):
            boyin = {"company":"boyin", "discount":'1.0', "inventory":'70', "price":'$10000000'}
            boyin2 = {"company":"boyin2", "discount":'1.0', "inventory":'100', "price":'$10000000'}
            tongyong = {"company":"tongyong", "discount":'0.9', "inventory":'500', "price":'$18000000'}
            return [boyin, boyin2, tongyong]
            
    b = BuySomeThing('飞机','200000000')
    b.showrResult()
