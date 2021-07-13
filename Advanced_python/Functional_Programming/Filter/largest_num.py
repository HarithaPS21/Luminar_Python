# lst=[2,3,4,8,10,7]     lst=[1,2,3,9,11,8]
lst=[2,3,4,8,10,7]
op=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(op)


lst.sort()