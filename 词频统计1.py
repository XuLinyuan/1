import collections,re  
def get_words(file):  
    with open (file,encoding='utf-8') as f:  
        words_box=[]  
        for line in f:   
            words_box.extend(re.split(r'[;\.\s]*', line))  
        new_words_box=[]  
        for word in words_box:  
            if word.isalpha():  
                new_words_box.append(word)   
    return collections.Counter(new_words_box)  
a=get_words('1.txt')+get_words('2.txt')+get_words('3.txt')+get_words('4.txt')+get_words('5.txt')
print(a.most_common(10))
