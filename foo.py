word = 'supercalifragilisticexpialidocious'
times = 0
for index in range(len(word)):
    if ('i' == word[index]):
        times = times  + 1
print(times)
print(("the length of %s is %d") % (word, len(word)))
