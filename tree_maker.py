import json 
import operator
import re
# failed attempt at making a tree

# def fun(lst, i):
# 	if i is len(lst) - 1:
# 	    return "("+unicode(lst[i][0])+":"+unicode(lst[i][1])+")"
# 	else:
# 		# if i is 0:
# 		#     return "("+unicode(lst[i][0])+":"+unicode(lst[i][1])+","+fun(lst, i+1)+")"
# 		# else:
# 	    return "("+unicode(lst[i][0])+":"+unicode(lst[i][1])+","+fun(lst, i+1)+")"
    
# with open('HD_data.json', 'rb') as fp:
# 	data = json.load(fp)
# 	save = []
# 	for a in data:
# 		x = data[a]
# 		sorted_x = sorted(x.items(), key=operator.itemgetter(1))
# 		save.append(sorted_x)
# 		# replacer = {}
# 		# r = "A"
# 		# for b in range(len(sorted_x)):
# 		# 	try:
# 		# 		sorted_x[b] = list(sorted_x[b])
# 		# 		sorted_x[b][0] = sorted_x[b][0].replace("(", "_")
# 		# 		sorted_x[b][0] = sorted_x[b][0].replace(")", "_")
# 		# 		s = str(sorted_x[b][0])
# 		# 	except:
# 		# 		replacer[r] = sorted_x[b][0]
# 		# 		sorted_x[b][0] = r
# 		# 		r = r + "A"
# 		# s = fun(sorted_x, 0)+";"
# 		# print s
# 		# t = Tree(s, format = 1);
# 		# print t
# 		# break


with open('HD_data.json', 'rb') as fp:
	with open('matrix_form.txt', 'wb') as fp2:
		data = json.load(fp)
		keyset = data.keys()
		fp2.write(str(len(data.keys())) + "\n")
		maxlen = 0
		# for a in keyset:
		# 	if len(a) > maxlen:
		# 		maxlen = len(a)
		# print maxlen
		for a in keyset:
			c = re.sub("[^a-zA-Z]+", "_", a)
			fp2.write('{:35s}\t'.format(c))
			for b in keyset:
				if a is b:
					fp2.write("0.0000\t")
				else:
					fp2.write("{:.4f}".format(data[a][b]) + "\t")
			fp2.write("\n")






