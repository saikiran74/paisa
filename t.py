def test(st):
    for i in range(2,len(st),2):
        if(st[0]==st[i] and st[1]==st[i+1]):
            count=1
        else:
            count=0
    if(count==1):
        print("YES")
    else:
        print("NO")
test("CDCDCD")