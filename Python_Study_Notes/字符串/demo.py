#作用
s1 = 'Tom say : "hi!Jackson"'
print s1

s2 = "cccaacc"
s3 = "aa"

if s3 in s2:
	print "s3 is in s2"

#字符串的访问 index, slice
s0 = "abcdefghijklmnopqrstuvwxyz"
print s0
print s0[6]

i = 0
while i < len(s0):
	print s0[i]
	i += 1
	
import random
i = 0
while i < 10:
	x = random.randint(100000, 1000000)
	s = str(x)
	if "4" in s:
		print i, "has 4 in ", s
	i += 1

#构造"a01b02c03...y25z26"




#ord('A')
s4 = "Houston Rockets"
i = 0
while i < len(s4):
	print s4[i], ord(s4[i])
	i += 1





