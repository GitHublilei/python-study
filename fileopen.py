f = open('somefile.txt', 'w')

f.write('Hello, ')

f.write('World')

f.close()

f = open('somefile.txt', 'r')

aaa = f.read(4)

bbb = f.read()

print(aaa + bbb)





























