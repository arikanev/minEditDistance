import numpy as np

def subcost(source_char, target_char):
	if source_char == target_char:
		return 0
	else:
		return 2

def backtrack(D):
	i = D.shape[0] - 1
	j = D.shape[1] - 1
	currPos = None
	ld = 0
	while currPos != 0:
		currPos = D[i,j]
		left = D[i,j-1]
		right = D[i-1,j]
		corner = D[i-1,j-1]
		minimum = min(left, right, corner)

		if currPos != minimum:
			ld += 1

		if minimum == D[i,j-1]:
		    currPos = D[i,j-1]
		    i = i
		    j = j-1
		elif minimum == D[i-1,j]:
			currPos = D[i-1,j]
			i = i-1
			j = j
		else:
			currPos = D[i-1,j-1]
			i = i-1
			j = j-1


	return ld


def minEditDistance(source, target):
	n = len(source)
	m = len(target)
	D = np.zeros((n + 1,m + 1))
	source = '#'+source
	target = '#'+target

	D[0,0] = 0
	for i in range(1, n + 1):
		D[i,0] = D[i-1,0] + 1
	for j in range(1, m + 1):
		D[0,j] = D[0,j-1] + 1

	for i in range(1,n + 1):
		for j in range(1,m + 1):
			D[i,j] = min(D[i-1,j]+1,D[i-1,j-1]+subcost(source[i], target[j]),D[i,j-1] + 1)

	return D 



D = minEditDistance("Apple", "Ankle")
print(D)
print(backtrack(D))
