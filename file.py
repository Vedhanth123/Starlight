# f=open("ved.txt")
# a=f.read()
# print(a)
# f.close()
with open ("ved.txt","w") as f:
    f.write("hello")
# f.close()
f=open("ved.txt","r")
print(f.tell())
print(f.readline())
f.seek(0)
print(f.readline())
