#i/p=[[1,2,3],[4,5,6]]  o/p:[1,2,3,4,5,6]
'''l1=[[1,2,3],[4,5,6]]
l2=[]
for e in l1:
    for i in e:
        l2.append(i)
print(l2)'''
#i/p:[1,2,3,4,5,6,7,8]  o/p:[[1],[2],[3],[4],[5],[6],[7],[8]]
'''l1=[1,2,3,4,5,6,7,8] 
l3=[]
for e in l1:
    l2=[]
    l2.append(e)
    l3.append(l2)
print(l3)'''
#o/p: [[1,2,3,4]
#       [5,6,7,8]
#       [9,10,11,12]]
'''l1=[]
k=1
for e in range(0,3):
   l2=[]
   for i in range(0,4):
        l2.append(k)
        k=k+1
   l1.append(l2)
print(l1)'''
#pythagoras triplet
'''count=0
for e in range(1,100):
    for i in range(1,100):
        for j in range(1,100):
            l=[]
            if(e**2==i**2+j**2):
                    l.append(e)
                    l.append(i)
                    l.append(j)
                    print(l)
                    count+=1
print(count)'''
#perfect number
'''for e in range(1,10000):
    l=[]
    sum=0
    for i in range(1,e):
        if(e%i==0):
            l.append(i)
    for k in l:
        sum=sum+k
    if(sum==e): 
        print(e)'''
#i/p:[[abc,pqr],[ap,qr]] S.T. how many times every letter has occured in the list
#l=[['abc','pqr'],['ap','qr']]
#l1=[],l2=[]
#def letter(alp): 
#    for e in l:
#        for i in e:
#            for j in i: 
#                l1.append(j) 
#    print(alp,l1.count(alp)) 
#letter('a')  
#letter('b')
#letter('c')
#letter('p')
#letter('q') 
#letter('r')
#zidane ka solution
#m=[['abc','pqr'],['ap','qr']]
#d=[]
#for i in m:
#	for j in i:
#		for k in j:
#			d.append(k)
#print(f"There were {len(d)} letter in the list")
#def letter_occur_in_list(to_count,passed_list):
#	return f"{to_count} occured {passed_list.count(to_count)} time in List"
#print(letter_occur_in_list('p',d))
    
#valley=[32123]
#l=[3, 2, 1, 2, 3]
#def odd(arg_list):
#    if len(arg_list)%2!=0:
#        return True 
#def reverse(arg_list):
#      arg_list= arg_list[::-1]
#      return arg_list
#def palindrome(arg_list):
#    if arg_list==reverse(arg_list): 
#        return True 
#def valley(arg_list):
#    if odd(arg_list) and palindrome(arg_list):
#        for e in range(0,3):
#            for i in arg_list:
#                if(arg_list[e]==i):
#                    print(i,end='')
#                else:
#                    print(end=' ')
#            print()
#valley(l)            
'''Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
       having solemnly resolved to constitute India into a SOVEREIGN, !
               SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
                and to secure to all its citizens'''                

a=[["WE, THE PEOPLE OF INDIA,"],["having solemnly resolved to constitute India into a SOVEREIGN, !"],["SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC"],["and to secure to all its citizens"]]
for e in a:
    for i in e:
#        print(i)
        if i=='having':
            print(i,start='\t')
    