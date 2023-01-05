## SNIPPETS 

## WRITING FILES
import boot_
f=open("myfile.txt","w") # opens a file for writing.
f.write("some data! Hooray data!")
f.close()

## READING FILES
import boot_
import os
os.listdir() # just for fun, get a list of existing files
f=open("myfile.txt","r")
print(f.read())
f.close()