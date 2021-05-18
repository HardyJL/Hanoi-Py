import os

class Disk:
    size: int = 0
    def __init__(self, value: int) -> None:
        self.size = value
    def __str__(self) -> str:
        return str(self.size)

class Tower:
    name: str = ""   
    def __init__(self, value: str) -> None:
        self.name = value
        self.disks: list[Disk] = []
    def __str__(self) -> str:
        cache = f"Tower{self.name} = (|"
        for i in self.disks:
            cache += str(i.size) + "|"
        cache += ")"
        return cache

def hanoi(n, source: Tower, helper: Tower, target: Tower):
    if n > 0:
        hanoi(n - 1, source, target, helper)        
        if source:
            target.disks.append(source.disks.pop())
            print(f"Moving Disk:({str(n)}) from Tower: {source.name} to Tower: {target.name}")        
        hanoi(n - 1, helper, source, target)

def populate(amount: int, tower: Tower) -> any:
    for i in range(amount, 0, -1):
        tower.disks.append(Disk(i))

while True:
    print("Enter the amount of disks!")
    inp = input()

    try:
        amount = int(inp)
    except ValueError:
        amount = 0
        print("Please enter a valid amount!")

    if amount:
        source = Tower("1")
        helper = Tower("2")
        target = Tower("3")

        populate(amount, source)
        hanoi(amount, source, helper, target)
        print (source, helper, target)

    
    input("Press 'Enter' to continue")
    os.system("clear")
    