def most_frequent(string):
    a= {}
    for i in string:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    sorted_frequency =sorted(a.items(),key=lambda x:x[1],reverse=True)
    for item in sorted_frequency:
        print(item[0],'=',item[1])
string ="Mississippi"
most_frequent(string)
