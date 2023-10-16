import os
 
def communication(child_writes):
 r, w = os.pipe() 
 processid = os.fork()
 if processid>0: 
   os.close(w)
   r = os.fdopen(r)
   print ("Parent reading")
   str = r.read()
   print( "Parent reads =", str)
 else:
   os.close(r)
   w = os.fdopen(w, 'w')
   print ("Child writing")
   w.write(child_writes)
   print("Child writes = ",child_writes)
   w.close()
 
 
str1 = "Hi parent! How are You"
communication(str1)
