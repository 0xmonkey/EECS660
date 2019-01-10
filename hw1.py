def S(N):
	A = []
	for n in range(2, N + 1):
		do_add_n = True
		for a in A:
			print ('a is ' + str(a))
			if n % a == 0:
				do_add_n = False
				break
		if do_add_n:
			A.append(n)
	return A
	
print ('the solution is ' + str(S(100)))