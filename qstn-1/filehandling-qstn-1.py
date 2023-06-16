f=open('words.txt','w')
f.write('python is a programming language')

f.close()
a=open('words.txt','r')
read=a.read()
print(read)

b=(read.split())
print(len(b))
