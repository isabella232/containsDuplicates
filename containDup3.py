def main():
	nums = [1,2,3,1]
	k = 3
	t = 0
	print(containsNearDup(nums,k,t))


def containsNearDup(nums,k,t):
	# using a similar method to buckets algorithm

	if t < 0:			# can't have a negative difference since we want abs val
	    return False
	d = {} 				# dictionary will map indices to values, using it as a window as big as k
	w = t+1 			# width of our buckets
	n = len(nums)
	for i in range(n):
		m = nums[i] / w 	# m will be the value of where it will be stored in the bucket
		if m in d:
			return True
		if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
			return True
		if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
			return True

		d[m] = nums[i]							# adding m into the dict

		if i >= k: del d[nums[i - k] / w]		# shrinking our window to its appropriate size
	return False

main()