from ete2 import Tree
import json 
import operator
def fun(lst, i):
	if i is len(lst) - 1:
	    return "("+unicode(lst[i][0])+":"+unicode(lst[i][1])+")"
	else:
		# if i is 0:
		#     return "("+unicode(lst[i][0])+":"+unicode(lst[i][1])+","+fun(lst, i+1)+")"
		# else:
	    return "("+unicode(lst[i][0])+":"+unicode(lst[i][1])+","+fun(lst, i+1)+")"
    

with open('HD_data.json', 'rb') as fp:
	data = json.load(fp)
	for a in data:
		x = data[a]
		sorted_x = sorted(x.items(), key=operator.itemgetter(1))
		replacer = {}
		r = "A"
		for b in range(len(sorted_x)):
			try:
				sorted_x[b] = list(sorted_x[b])
				sorted_x[b][0] = sorted_x[b][0].replace("(", "_")
				sorted_x[b][0] = sorted_x[b][0].replace(")", "_")
				s = str(sorted_x[b][0])
			except:
				replacer[r] = sorted_x[b][0]
				sorted_x[b][0] = r
				r = r + "A"
		s = fun(sorted_x, 0)+";"
		print s
		t = Tree(s, format = 1);
		print t
		break
