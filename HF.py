import json
props = set([])
num_data = {}
with open('named_data.json', 'rb') as fp:
	data = json.load(fp)
	for lang in data:
		for prop in data[lang]:
			if prop not in props:
				props.add(prop)

	for lang in data:
		res = ""
		for p in props:
			if p in data[lang]:
				if 'Yes' in data[lang][p]:
					res = res + "1"
			else:
				res = res + "0"
		print res
		num_data[lang] = int(res, 2)

def hamming_distance(a, b):
	dist = 0
	val = a ^ b
	print b
	while val is not 0:
		dist = dist +1
		val = val & (val-1)
	return dist

d = {}
for a in num_data:
	d2 = {}
	for b in num_data:
		if a is not b:
			print a
			d2[b] = hamming_distance(num_data[a], num_data[b])
	d[a] = d2


with open('HD_data.json', 'wb') as fp2:
	json.dump(d, fp2)

