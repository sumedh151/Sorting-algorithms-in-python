def swap(list , pos1 , pos2):
	list[pos1] , list [pos2] = list[pos2] , list [pos1]
	return list

def selection_sort(list):
	for i in range(0 , len(a)-1):
		k = i
		for j in range(i , len(a)):
			if list[j] < list[k]:
				k = j
		swap(list , k , i)
	return list


a = [2,7,4,1,5,3]
print(a)
selection_sort(a)
print(a)
