def xrange(min, max=0):
	o = 0
	if max == 0:
		while o < min:
			yield o
			o += 1
	else:
		if min < max:
			while min < max:
				yield min
				min += 1
		else:
			print("输入值非法")


def demo():
	for i in range(10):
		yield print(i)


a = demo()
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)