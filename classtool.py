class AttrDisplay:
    """docstring for AttrDisplay"""
    def getAllAttrs(self):
        lists = []
        for key in sorted(self.__dict__):
            lists.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(lists)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.getAllAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
    class SubTest(AttrDisplay):
        pass

    X,Y = TopTest(), SubTest()
    print(X, Y, sep='\n')
