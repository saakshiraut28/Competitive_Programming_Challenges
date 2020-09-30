Max = int(input("No. of gold coins - "))
if Max%3==0:
    print("Yes, They can be distributed equally")
    lis = set()
    ary = []
    ary.append(1)
    lis.add(1)
    ary.append(2)
    lis.add(2)
    for i in range(3, Max):
        count = 0
        for j in range(0, len(ary)): 
            if (i - ary[j]) in lis and ary[j] != (i - ary[j]):  
                count += 1
            if count > 2:
                break
        if count == 2: 
            ary.append(i)  
            lis.add(i)  
    print("Count of individual kid: ",ary)
else:
    print("Can't be distributed equally.")


