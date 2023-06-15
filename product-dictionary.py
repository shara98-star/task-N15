n=int((input("how many products:?")))
price_list=[]
lists=[]
product_list=[]
for  index,_ in enumerate(range(n),1):
    product={}
    print(f"\n product n{index}")
    product["product"]=input("product")
    product["price"]=int(input("price"))
    price_list.append(product["price"])
    product_list.append(product["product"])
    lists.append(product)
keys=price_list
values=product_list
dictionary=dict(zip(keys,values))
print(f"the most expensive product is : {dictionary[max(price_list)]}")
print(f"the cheapest product is: {dictionary[min(price_list)]}")
for i in dictionary:
    if price_list.count(i)>1:
        print(f"there are more than one with same prices ,for example :{dictionary[i]}")  
