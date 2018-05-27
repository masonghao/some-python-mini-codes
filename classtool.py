class AttrDisplay:
    """
    Provides an inheritable print voerload method that displays
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its calsses). Can be mixed into any class,
    and will work in any instance.
    """
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
    print(X, Y, sep='\n') # Show all instance attrs, show lowest class name
