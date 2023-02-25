class Ayush:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        print(f"My name is {self.name}")
        
a = Ayush("arpit")
a.getname()
3
mylist = list(map(int,input("Enter the numbers :").split())) 
for i in mylist:
    print(i)