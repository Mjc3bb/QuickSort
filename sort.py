set = [10,9,8,7,6,5,4,3,2,1,0]

def sortList(sortSet):
	if (len(sortSet)<=3):
		sortSet.sort()
		return sortSet
	else:
		a = len(sortSet)/2
		a = int(a)
		l1 = sortList(sortSet[0:a])
		l2 = sortList(sortSet[a:len(sortSet)])
		tempSet = []
		while (len(l1)!= 0 and len(l2) != 0):
			if (len(l1)==0 or len(l2)==0):
				tempSet+l1+l2
			b = l1[0]
			c = l2[0]
			if(b<c):
				x=l1[0]
				tempSet.append(b);l1.remove(b)
			elif(b>c):
				x=l2[0]
				tempSet.append(c);l2.remove(c)
			else:
				tempSet.append(b)
				tempSet.append(c)
				l1.remove(b)
				l2.remove(c)
		return tempSet
	
print sortList(set)
