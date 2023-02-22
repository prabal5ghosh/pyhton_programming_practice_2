# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 10 
# Expected Result : 102030
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
print(n1)
n2 = int( "%s%s" % (a,a) )
print(n2)
n3 = int( "%s%s%s" % (a,a,a) )
print(n3)
print (n1+n2+n3)