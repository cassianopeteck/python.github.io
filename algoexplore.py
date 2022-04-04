def isValidSubsequence(array, sequence):
    # Write your code here.
	check = 0
	
	for i in array:
        for j in sequence:
            if i == j:
                check+=1
                continue
	

	if(check == len(sequence)):
		return True
	else:
		return False


print(isValidSubsequence([6,-1,8,10],[8,-1,10]))