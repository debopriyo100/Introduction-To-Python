list = [i*i for i in range(1,11) if i%2==0]
print(list)

names = ["Ben","Elizabeth","Orange","Di","Gn"]
length = {name :len(name) for name in names}
print(length)
letters = [name for name in names if len(name)>3]
print(letters)



price = [14,21,156,91, 210, 329]
with_tax = [round(p*1.2,5)for p in price if p>100]
print(with_tax)