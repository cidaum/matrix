# Please fill out this stencil and submit using the provided submission script.




## Problem 1
def myFilter(L, num): return [x for x in L if x%num !=0 or x<num]



## Problem 2
def myLists(L): return [list(range(1,x+1)) for x in L]



## Problem 3
def myFunctionComposition(f, g): return {x:g[y] for (x,y) in f.items()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (3 + 1j) + (2 + 2j)
complex_addition_b = (-1 + 2j) + (1 -1j)
complex_addition_c = (2 + 0j) + (-3 + .001j)
complex_addition_d = 4*(0 + 2j) + (.001 + 1j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
	retorno = 0
	for valor in L:
		retorno += valor
	return retorno



## Problem 7
def myProduct(L):
	retorno = 1
	for valor in L:
		retorno = retorno * valor
	return retorno


## Problem 8
def myMin(L):
	retorno = L[0]
	for item in L[1:]:
		if item < retorno:
			retorno = item
	return retorno


## Problem 9
def myConcat(L):
	retorno = L[0]
	for item in L[1:]:
		retorno = retorno+item
	return retorno


## Problem 10
def myUnion(L):
	retorno = set({})
	for item in L:
		retorno.update(item)
	return retorno
