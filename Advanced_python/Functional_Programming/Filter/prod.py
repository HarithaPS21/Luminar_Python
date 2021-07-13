products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]

out_stock=list(filter(lambda product:product["stock"]==0,products))
print(out_stock)

details=list(filter(lambda product:product["mrp"]<250,products))
print(details)

# details of all products below 250
