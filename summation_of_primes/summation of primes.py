import eulerlib
def compute():
	ans = sum(eulerlib.list_primes(1999999))
	return str(ans)


if __name__ == "__main__":
	print(compute())