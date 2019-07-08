import shelve
#
# with open('aurora.jpg','rb') as rf:
# 	with open('new_aurora.jpg','wb') as wf:
# 		chunk_size = 4096
# 		rf_chunk = rf.read(chunk_size)
# 		while len(rf_chunk) > 0:
# 			wf.write(rf_chunk)
# 			rf_chunk = rf.read(chunk_size)

# rf = open('Doris Day - Que Sera Sera.mp3','rb')
# wf = open('copy_Doris Day - Que Sera Sera.mp3','wb')
#
# chunk_size = 4096
# rf_chunk = rf.read(chunk_size)
# while len(rf_chunk) > 0:
# 	wf.write(rf_chunk)
# 	rf_chunk = rf.read(chunk_size)
#
# rf.close()
# wf.close()


# with open('Young God.mp3','rb') as rf:
# 	with open('Young God_copy.mp3','wb') as wf:
# 		chunk_size = 4096
# 		rf_chunk = rf.read(chunk_size)
# 		while len(rf_chunk) > 0:
# 			wf.write(rf_chunk)
# 			rf_chunk = rf.read(chunk_size)


#Shelf values don’t have to be opened in read or write mode
# they can do both once opened.
shelfFile = shelve.open('myCat')
# The value of shelfFile is dictionary type
cats = ['Garfield','Tom','Kitty']
shelfFile['cats'] = cats
shelfFile.close()


shelfFile = shelve.open('myCat')
print(type(shelfFile))
print(shelfFile['cats'])
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

