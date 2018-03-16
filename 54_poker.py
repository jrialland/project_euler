
cards = '23456789TJQKA'

def highCard(h):
    return max(map(lambda c:1+cards.index(c),map(lambda c:c[0], h)))

def _sameVal(h,m=2):
	sort = {v[0]:[] for v in h}
	for v in h:
		sort[v[0]].append(v)
	l = [sort[c] for c in cards if ''.join(h).count(c) == m]
	for d in l:
		if len(d)==m:
			return d
	return None

def onePair(h):
	p = _sameVal(h,2)
	if p is None:
		return 0
	else:
		return 1+cards.index(p[0][0])

def twoPairs(h):
	p = _sameVal(h,2)
	if p:
		h2 = h[:]
		h2.remove(p[0])
		h2.remove(p[1])
		p2 = _sameVal(h2,2)
		if p2:
			return max(1+cards.index(p[0][0]),cards.index(p2[0][0]))
	return 0

def threeOfAKind(h):
	p = _sameVal(h,3)
	if p is None:
		return 0
	else:
		return 1+cards.index(p[0][0])

def straight(h):
	l = sorted(map(lambda i:1+cards.index(i),map(lambda c:c[0], h)))
	for i in range(1, 5):
		if l[i] != l[i-1]+1:
			return 0
	return max(l)

def flush(h):
	s = map(lambda c:c[1], h)
	return int(s in ['H'*5,'C'*5,'S'*5,'D'*5])

def fullHouse(h):
	pair = onePair(h)
	_3k = threeOfAKind(h)
	if pair and _3k:
		return _3k + pair/14.0
	else:
		return 0

def fourOfAKind(h):
	p = _sameVal(h,4)
	if p is None:
		return 0
	else:
		return 1+cards.index(p[0][0])

def royalFlush(h):
	f = ''.join(sorted(map(lambda c:c[0], h)))
	return int(f == 'AJKQT' and flush(h))


def score(h):
	tests = [
		highCard,
		onePair,
		twoPairs,
		threeOfAKind,
		straight,
		flush,
		fullHouse,
		fourOfAKind,
		royalFlush
	]
	s = [v*(14**i) for i, v in enumerate(map(lambda t:t(h), tests))]
	return max(s)

def read():
	with open('p054_poker.txt') as f:
		for line in f:
			data = line.strip().split()
			player1 = data[:5]
			player2 = data[5:]
			if score(player1) > score(player2):
				yield 1

print sum(read())
