import threading
def fun1(a, b):
 c = a + b
 print("\nthread 1",c)
def fun2(a, b):
 c = a - b
 print("\nthread 2",c)
thread1 = threading.Thread(target = fun1, args = (12, 10))
thread2 = threading.Thread(target = fun2, args = (12, 10))
thread1.start()
thread2.start()
