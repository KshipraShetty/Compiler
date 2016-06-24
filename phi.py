f1=open('block1.txt','r')
dicti={}
a=[]
f1=open('block1.txt','r')
line1=1
f1.next()
for line in f1:	
	if not line.strip().isdigit():
		lin=line.strip()
		a.append(lin)
	else: 
		a=[]
		line1=line.strip()
	dicti.update({int(line1):a})	
print dicti
f1.close()
print("\n\n")
f1=open('df.txt','r')

for line in f1:
	line.strip()
	lin=line.split(" ")
	#i=0
	for values in dicti[int(lin[0])]:
		if values.find(" = ")!=-1:
			lin1=values.split(" ")
			obj="phi("+str(lin1[0])+","+str(lin1[0])+")"
			dicti[int(lin[0])]=[obj]+dicti[int(lin[0])]
			
	
print dicti
