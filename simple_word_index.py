from collections import Counter
text = "apple and banana one apple one banana a red apple and a green apple"
word_list = text.split()
words_count = Counter(word_list) 
for k,v in words_count.items():
    print( f"|{k:{len(max(word_list, key=len))}}| {v:.0f} |")
