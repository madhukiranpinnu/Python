import Pack1.file
Pack1.file.f1()
from Pack1.file import f1
f1()
import Pack1.Inner.Module2
Pack1.Inner.Module2.f2()
from Pack1.Inner.Module2 import *
f2()