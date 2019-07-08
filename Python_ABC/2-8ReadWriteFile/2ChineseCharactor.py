with open('Jeanette_c.txt','w',encoding='utf-8') as f:
	f.write('''我会给你电话，我们一起生个火，喝点小酒，在属于我们的地方辨认彼此。
别等待，别把故事留到后面讲，生命如此之短。这一片海和沙滩，这海滩上的散步，在潮水将我们所做的一切吞噬之前。 
我爱你。 
这是世上最难的三个字。 可除此以外。我还能说什么。''')

with open('Jeanette_c.txt','r',encoding='utf-8') as f:
	s = f.read()
	print(s)