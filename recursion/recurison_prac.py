import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())

i = 0


def myfun():
    global i
    i=i+1
    print("my func", i)
    myfun()

myfun()

