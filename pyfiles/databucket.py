#should I make this?
class databucket:
    bucketname = "myfirstbucket"
    filename = "Iris"
    data = None

    def __init__(self, buck = "myfirstbucket", dataset = "Iris"):
        self.bucketname = buck
        self.filename = dataset

    def setbuck(self, buck):
        self.bucketname = buck
    def getbuck(self):
        return(self.bucketname)

    def setfile(self, dataset):
        self.filename = dataset
    def getfile(self):
        return(self.filename)

    def setdata(self, newdata):
        self.data = data

    def getdata(self):
        return(self.data)