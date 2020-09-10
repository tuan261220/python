n = int(input('nhap so n ='))
a = ''
for i in range (1,n):
    for j in range (i+1,n):
        for k in range(j+1,n):
            if(i*i + j*j == k*k):
                print("("+str(i)+", " + str(j) +", " + str(k)+")")
