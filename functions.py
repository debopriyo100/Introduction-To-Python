def count_occ(val,item):
    count=0
    for i in val:
        if i ==item:
            count+=1
    return count
def filter_val(val,min):
    return{k: v for k, v in val.items()if v>=min}
print(filter_val({"anc": 8 , "cup":10 ,"plate": 5}, 11))