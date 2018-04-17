def wordcount(str):
    # 文章字符串前期处理
    str_list = str.replace('\n', '').lower().split(' ')
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for str in str_list:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)

    return count_list
str_context=open ('1.txt').read()
rank=wordcount(str_context)
for word in rank[0:10]:
    print(word)