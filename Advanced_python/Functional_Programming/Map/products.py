

# list all product names

products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]
product_name=map(lambda product:product["item_name"],products)
print(list(product_name))

# for product in products:
#   print(product["item_name"])

