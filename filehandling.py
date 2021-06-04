#opening a file

fileobj=open("abc.txt","wb")

print("Name of the file:",fileobj.name)
print("closed or not:",fileobj.close)
print("opening mode:",fileobj.mode)

#closing file

fileobj=open("abc.txt","wb")
print("Name of the file:",fileobj.name)

fileobj.close()

#writing a file

fileobj=open("abc.txt","w")
fileobj.write('super power\n')
fileobj.write('iron man\n')

#with statement

with open("abc.txt","r") as fileobj:
   content=fileobj.read();
   print(content)

#reading a file

fileobj=open("abc.txt")
fileobj.read()
