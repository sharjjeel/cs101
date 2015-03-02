import urllib2
import json

# url = "http://sswl.railsplayground.net/browse/languages/"
# usock = urllib2.urlopen(url)
# content=usock.read()
# sp = content.split("\n")
# for a in sp:
# 	if "href" in a and "languages" in a:
# 		st = a.index("href=")
# 		p = a[st+6:]
# 		st2 = p.index(">");
# 		print(p[:st2-1])

# f = open('websites.txt', 'r')
# upper_dic = {}
# for line in f:
# 	url = line
# 	print(url)
# 	usock = urllib2.urlopen(url)
# 	content=usock.read()
# 	sp = content.split("\n")
# 	v = False
# 	dic = {}
# 	name = ""
# 	for a in sp:
# 		if ("href" in a and "/properties/" in a):
# 			if v:
# 				raise Exception("OUT OF ORDER")
# 			v = True
# 			s = a.index("\"")
# 			e = a.index(">")
# 			ul = a[s:e-1]
# 			name = a[e+1:]
# 			e = name.index("<")
# 			name = name[:e]
# 		elif "width=\"100px" in a and ("Yes" in a or "No" in a or "NA" in a or "no" in a or "yes" in a):
# 			if not v:
# 				raise Exception("OUT OF ORDER")
# 			v = False
# 			s = a.index(">")
# 			res = a[s+1:]
# 			res = res[:res.index("<")]
# 			dic[name] = res
# 	upper_dic[url] = dic
# with open('data.json', 'wb') as fp:
#     json.dump(upper_dic, fp)

with open('data.json', 'rb') as fp:
	data = json.load(fp)
	d = {}
	for a in data:
		usock = urllib2.urlopen(a)
		content=usock.read()
		sp = content.split("\n")
		res = "NA"
		for b in sp:
			if "class=\"floatLeftWhite\">" in b:
				s = b.index(">")
				res = b[s+1:]
				res = res[:res.index("<")]
				print(res)
				break
		if res in d or res is "NA":
			raise Exception("invalid name")
		d[res] = data[a]
	with open('named_data.json', 'wb') as fp2:
		json.dump(d, fp2)
	assert(len(d) == len(data))