def main():
    q="sOuk;iDet4geKaw8;CY5tjA"
    a=[]
    for i in q:
        a.append(i)
    print(a)
    a2=8%6+2
    for i in range(0,len(q),3):
        if ord(a[i])>96 and ord(a[i]) <=122:
            a[i]=chr(((ord(a[i]))+84-a2-12)%26+97)
        elif ord(a[i])>64 and ord(a[i])<=90:
            a[i]=chr(((ord(a[i]))+52-a2)%26+65)
    print(a)
    for k in range(len(q)):
        if ord(a[k])-a2>47 and ord(a[k])-a2<=57:
            a[k]=chr(ord(a[k])-a2)
    print(a)
    h=""
    c=[]
    for j in range(len(q)): 
        c.append(a[(j-a2)%len(q)])
    o=""
    for i in range(len(q)):
        if ord(c[i])==0:
            c[i]=chr(10)
    for i in range(len(q)):
        o+=c[i]
    print(o)
main()
