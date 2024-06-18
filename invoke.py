def myfun1():
    print("Executing myfun1...")

def myfun2():
    print("Executing myfun2...")
    myfun1()

myfun2()