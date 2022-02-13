import math

def bsgs(p: int, g: int, x: int):
	"""
	Equation g^L = x mod p is solved wrt. L

	"""
	m = math.floor(math.sqrt(p))

	g_j = {pow(g,j,p): j for j in range(1, m+1)}

	for i in range(1, m+1):
    		y = pow(g, -i*m, p) * x % p
    		if g_j.get(y):
        		return i*m+g_j.get(y)


if __name__ == '__main__':
	p = 17393
	g = 2135
	x = 5999

	print(bsgs(p, g, x))
