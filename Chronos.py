class Chronos:
    def __init__(self, name = False):
        self.timer = list()
        self.name = list()
        self.step = 0
        try :
            self.newChronos(name)
        except NameError:
            import time
            global time
            self.newChronos(name)

    def newChronos(self, name=False):
        self.timer.append(time.time())
        if not name : 
            self.name.append(self.step)
        else:
            self.name.append(name)
        self.step += 1

    def printChronos(self):
        for i in range(1,len(self.timer)):
            print(f"{self.name[i]} : {self.timer[i] - self.timer[i-1]}  ")
