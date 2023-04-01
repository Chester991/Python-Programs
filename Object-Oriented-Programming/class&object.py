class Student :
    # here why am i initializing name to Ayush if out put is about priyanshu/Tuli
    name = "Ayush"
    passion = "CP"
    isdetained = False
    def info(self) :
        print(f"{self.name} is passionate about {self.passion}")
        # self means that object for which this method (.name,.passion) is called

a = Student()
b = Student()

a.name = "Priyanshu"
a.passion = "Girls"

b.name = "Tuli"
b.passion = "CP"

a.info() # here a will replace self
b.info()

# output: Priyanshu is passionate about Girls Tuli is passionate about CP