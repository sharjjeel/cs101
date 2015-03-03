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
			if p in data[lang] and (data[lang][p] is 'Yes' or data[lang][p] is 'yes'):
				res = res + "1"
			else:
				res = res + "0"
		num_data[lang] = int(res, 2)

def hamming_distance( a, b):
	dist = 0
	val = a ^ b
	while val is not 0:
		dist = dist +1
		val = val & (val-1)
	return dist

d = {}
for a in num_data:
	d2 = {}
	for b in num_data:
		if a is not b:
			d2[b] = hamming_distance(num_data[a], num_data[b])
			if d2[b] is not 0:
				print a
				print b
	d[a] = d2


with open('HD_data.json', 'wb') as fp2:
	json.dump(d, fp2)

