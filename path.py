from MathGraph import MathGraph

def addbefore(l, s):
	for n in range(len(l)):
		l[n] = [s] + l[n]
	return l

def get_path(g, vertex):
	if g.connection[g.dict2[vertex]] == []:
		return [[vertex]]
	res = []
	for n in g.connection[g.dict2[vertex]]:
		a = get_path(g, g.dict1[n])
		res = res + addbefore(a, vertex)
		return res

def searchbegin(g):
	l = list(g.dict2)
	for n in g.dict2:
		for m in range(len(g.connection)):
			if g.dict2[n] in g.connection[m]:
				if n in l:
					l.remove(n)
	return l

def path(g):
	a = []
	for n in range(len(searchbegin(g))):
		a = a + get_path(g, searchbegin(g)[n])
	return a