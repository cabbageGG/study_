#-*- coding: utf-8 -*-

# author: li yangjin

from multiprocessing import Process
import os

def test_pro(*args, **kw):
    print (args)
    print (kw)
    print("%s child Processor %s is running (%s)" % (kw.keys()[0], args[0], os.getpid()))

if __name__ == "__main__":
    print("Parent Processor is running (%s)" % os.getpid())
    p = Process(target=test_pro, args=("test",),kwargs={"hello":1})
    p.start()
    p.join()
    print ("end")