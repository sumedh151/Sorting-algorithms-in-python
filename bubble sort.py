def swap(list , pos1 , pos2):
	list[pos1] , list [pos2] = list[pos2] , list [pos1]
	return list

def bubble_sort(list):
	for i in range(0 , len(list)-1):
		for j in range(0,len(list)-1 - i):
			if list[j] > list[j+1]:
				list = swap(list , j , j+1)
	return list


a = [2,7,4,1,5,3]
print(a)
bubble_sort(a)
print(a)

