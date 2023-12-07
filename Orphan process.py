import os, sys, time
ttlForParent = 50;
for i in range(0, 10):
  pid_1 = os.fork()
  print("Hello Worlds!!!")
  if pid_1 == 0:
    sys.exit();
  
time.sleep(ttlForParent);
os.wait()
