import os
from time import sleep
pid=os.fork()
if(pid==0):
  print("child process id",os.getppid(),os.getppid())                                                                                                                                     
elif(pid>0):
  sleep(5)
  print("parent process id",os.getppid(),os.getppid())
else:
  print("process is not created")
