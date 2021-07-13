from functools import reduce
products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]
prices=list(map(lambda p1,p2:p1 if p1>p2 else p2))
high_cost=reduce(lambda price1,price2:price1 if price>price2 else price2)
print(high_cost)