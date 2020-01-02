def main():

	nums = [1,2,3,2,4,5]
	print(ContainsDupes(nums))

def ContainsDupes(nums):
	return len(nums) > len(set(nums))

main()
