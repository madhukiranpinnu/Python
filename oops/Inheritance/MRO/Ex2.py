class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B):
    pass
class E(A,B):
    pass
class F(D,E,C):
    pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())
