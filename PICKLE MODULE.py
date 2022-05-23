import pickle


class Employee:
    def __init__(self, eno, ename, esal, eaddrs):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddrs = eaddrs

    def Display(self):
        print('eno:{} , ename:{} , esal:{} , eaddrs:{}'.format(self.eno, self.ename, self.esal, self.eaddrs))


# creating object
e = Employee(100, "madhav", 10000, "pune")

# performing serialization
with open("emp.ser", "wb") as f:
    pickle.dump(e, f)

# performing serialization
with open("emp.ser", "rb") as f:
    newObj = pickle.load(f)

newObj.Display()
