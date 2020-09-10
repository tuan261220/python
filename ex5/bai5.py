class AnyClass:
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

    def __str__(self):
        attrs = ["%s=%s"%(k,v) for (k,v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s : %s" % (classname, ",".join(attrs))


# sample = AnyClass(name = "Nam",age = 18)
# print(sample)
# sample1 = AnyClass(Brand = "HONDA", name = "SH", price = 10000)
# print(sample1)



