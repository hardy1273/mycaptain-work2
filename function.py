def  most_frequent():
    a=input("Enter a string")
    b=list(a)
    count=0
    d={}
    for i in range(len(b)):
        if b[i-1]==b[i]:
            s=b.count(b[i])
            d[b[i]]=s
        else:
            s=b.count(b[i])
            d[b[i]]=s
    x=list(d.items())
    x.sort(reverse=True)
    d1=dict(x)
    print(d1)
        
most_frequent()
