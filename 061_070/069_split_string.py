str3 = " while JJ is sleeping, his parents are working. "
words_lists = str3.split()
print(words_lists)

str3 = " while,JJ,is,sleeping,his,parents,are,working. "
words_lists = str3.split(',')
print(words_lists)

str3 = " while.JJ.cv "
words_lists = str3.split()
print(words_lists)

str3 = " while.JJ.cv "
words_lists = str3.split('.')
print(words_lists)