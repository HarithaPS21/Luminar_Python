
# count of each word in the file "book"

f1=open("book","r")
count={}
for i in f1:
    words=i.rstrip("\n").split(" ")
    # print(words)
    for word in words:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)

