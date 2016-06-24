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
dict=dicti.copy()
f1.close()


print("\n\n")
f1=open('df.txt','r')
dictio={}
for line in f1:
	line.strip()
	lin=line.split(" ")
	for values in dicti[int(lin[0])]:
		if values.find(" = ")!=-1:
			lin1=values.split(" ")
			obj="phi("+str(lin1[0])+","+str(lin1[0])+")"
			for i in range(1,len(lin)-1):
				if obj not in dicti[int(lin[i])]:				
					lin[i].strip()
				
					dicti[int(lin[i])]=[obj]+dicti[int(lin[i])]
		else:
			dicti[int(lin[0])]=(dicti[int(lin[0])])
print dicti
