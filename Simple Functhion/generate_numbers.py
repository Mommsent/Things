def generate_numbers (N:int, M:int, prefix=None):
	#Генерирует все числа (с лидирующими незначащими нулями)
 	#в N-ричной системе счисления N <= 10 длинны M
	prefix = prefix or []

	if M == 0:
		print(prefix)
		return

	for digit in range (N):
		prefix.append(digit)
		generate_numbers(N, M - 1, prefix)
		prefix.pop()

generate_numbers(4,3)

def gen_bin(M, prefix = ""):
	if M == 0:
		print(prefix)
	gen_bin(M - 1, prefix + "0")
	gen_bin(M - 1, prefix + "1")