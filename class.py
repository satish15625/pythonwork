class A():
    print("A")
class B():
    print("B")

class C(B,A):
    pass

c = C()
c.C()

