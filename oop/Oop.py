class Student(object):
    
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd
    def talk(self):
        print(self.uname+"----"+self.pwd+"---"+self.no)


if __name__ == '__main__':
    sd = Student("good","666")
    sd.talk()
    sd.no = "999"



