'''
mystr = 'Sa'
x=len(mystr)
y=mystr[len(mystr)-2:-1]
print(x)
print(y)
'''
def Selectivelist(list1):
	newlist = [ ]
	for i in list1:
		if(i > 10):
			l1=str(i)
			c=int(l1[len(l1)-2:-1])
			if(c==7):
				if(i%41==0):
					newlist.append(i)
	print(newlist)
	return(newlist)

Mylist1=[45,33,7777,78,374,24,574,764548576,779]
list2=Selectivelist(Mylist1)


offile = "Harshout1.txt"
outf = open(offile,"w")

for i in list2:
	l1=str(i)
	print(l1)
	outf.write("%s\n" % l1)


