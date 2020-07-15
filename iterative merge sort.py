def merge(b , low , high , mid):
	i = low
	j = mid + 1
	new_list = list()

	while i <= mid and j <= high:
		if b[i] < b[j]:
			new_list.append(b[i])
			i+=1
		else:
			new_list.append(b[j])
			j+=1

	while (i<=mid):
		new_list.append(b[i])
		i+=1

	while (j<=high):
		new_list.append(b[j])
		j+=1

	x = low
	for i in new_list:
		b[x] = i
		x+=1

	return b

def iterative_merge_sort(a):
	n = len(a)
	p = 2
	while (p<=n):
		i = 0
		while (i+p-1 < n):
			l = i
			h = i+p-1
			mid = (l+h)//2
			merge(a , l , h , mid)
			i+=p
		p*=2
	if p//2 < n:
		merge(a , 0 , (p//2)-1 , n-1)

	# return a


a = [8,3,7,4,5,2,6,5]
# a = [100,1,2,20,3,4,4,15,5,6,17,12,7,10,7,9]
print(a)
iterative_merge_sort(a)
print(a)