#default mode is read
#if we use this method then we don't have to close the file
#with open('seitb2.txt','r') as f:
##    once we move out of this block the file closes
#    a=f.readline()
#    print(a)
#    print(f.tell())
#in f.read(size)---size=how many characters we want to print from the file
    #f.tell--tells us how many characters it read
    #f.seek--change the position to any location wherever we want it to be
#if we want to copy pics then we have to convert it into binary mode
#forthat we ahve to write 'rb' or'wb' instead of 'r' or'w' 
#A MATRIX FILE--1)FIND THE SUM OF EACH ROW,2)SUM OF EACH COLUMN  
#with open('file.txt','w') as f:
#    for i in range(1,11):
#        for e in range(1,11):
#            f.write(str(e))
#            f.write('\t')
#        f.write('\n')
#-------for row addition-----------
##with open('file.txt','r') as t:
#    l1=[]
#    for h_num in t:
#        rem=h_num.split()
#        l1.append(rem)
#    print(l1)
#    for e in l1:
#        sum=0
#        for j in e:
#            sum+=int(j)
#        print(sum)
#-----------for column addition------------
with open('file.txt','r') as t:
    l1=[]
    for h_num in t:
        rem=h_num.split()
        l1.append(rem)
    print(l1)
    k=0 
    for e in range(len(l1[0])):
        sum=0
        for j in l1:
            sum+=int(j[k])
        k+=1
        print(sum)