import numpy as np
import string
with open('matrix_form.txt', 'rb') as fp:
	mat = np.zeros((253, 253))
	ct = 0
	frt = True
	keys = []
	for n in fp:
		a = np.array([])
		if frt:
			frt = False
			continue
		first = True
		i = 0
		for nf in n.split():
			if first:
				keys.append(nf)
				first = False
				continue
			else:
				mat[ct][i] = float(nf)
			i = i + 1
		ct = ct + 1
	print len(mat)
	print len(mat[0])
	d = (mat.transpose() == mat)
	for a in d:
		for b in a:
			if b == False:
				print "not distance matrix"

	dic = {}
	new_keys = []
	als = []
	for a in string.lowercase:
		for b in string.lowercase:
			als.append(a+b)
	ct = 0
	for k in keys:
		dic[k] = als[ct]
		ct = ct + 1
	with open("key.txt", "wb") as k:
		for a in keys:
			k.write(a+ ": " + dic[a] + "\n")
	# with open("rechecked_mat_form.txt", "wb") as fp2:
	# 	fp2.write(str(len(keys)) + "\n")
	# 	ct = 0
	# 	for a in keys:
	# 		s = "{:12s}".format(dic[a])
	# 		i = 0
	# 		for b in mat[ct]:
	# 			if i == 0:
	# 				s = s + "{:1.4f}".format(b)
	# 			else:
	# 				s = s + '\t' + "{:1.4f}".format(b)
	# 			i = i+1
	# 		fp2.write(s + "\n")
	# 		ct = ct + 1



	