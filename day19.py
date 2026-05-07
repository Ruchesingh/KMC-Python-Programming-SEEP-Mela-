
""""#unpythonic display the items which have less price than 5
us_price={'milk':2.05,'bread':2.6, 'butter':3.6, 'mobile':50, 'television':1000, 'refrigerator':700}
nep_price={}
for k,v in us_price.items():
    if v<5:
        nep_price.update({k:v})
print(nep_price)

#pythonic way
nep_price={
    k:v
    for k,v in us_price.items()
    if v<5
}
print(nep_price)

#price<5=> 13% tax
#20% tax
for k,v in us_price.items(): # unpythonic way
    if v<5:
        nep_price.update({k:round(v * 145 *1.13)})
    else:
            nep_price.update({k:round(v * 145 *1.20)}) 
print(nep_price)            
 #pythonic way
 
nep_price={k:round(v*145*1.13) if v<5 else round(v*145*1.20)
           for k,v in us_price.items()}
print(nep_price)"""