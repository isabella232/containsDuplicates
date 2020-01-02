def main():

	nums = [1,2,3,1,2,3]
	k = 2
	print(ContainsDupes(nums,k))

def ContainsDupes(nums,k):

	if (containsDup(nums) == True):
	    return absDiff(nums, k)
	else:
	    return False


def containsDup(nums):
    return len(nums) > len(set(nums))

def absDiff(nums, k):

    for i in range(len(nums)):
        duple = nums[i]
        for j in range(i +1, len(nums)):
            if nums[j] == duple:
                if(abs(j-i)<=k):
                    return True
    return False


main()