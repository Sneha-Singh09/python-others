print('(*-indicates grace marks given)')
name_list=[]
marks_list=[]
avg_list=[]
for e in range(1,3):
    print(str(e)+'.Enter name:')
    name=str(input())
    print('Enter marks out of 100 for Physics,Chemistry and Maths:')
    m=[]
    sum=0
    j=0
    for i in range(0,3): 
        marks=int(input())
        m.append(marks)
        sum+=marks
#to check if the person has passed or failed without grace marks
        if marks>=50:
            j+=1
        else:
            j=0
    avg=sum/3
    avg_list.append(round(avg,2))
    marks_list.append(m)
    name_list.append(name)
    print('NAME:'+name)
    print('Marks:'+str(m)) 
    print('Average: {0:.2f}'.format(avg))
    if j==3 and avg>=50:
        print('PASS')
    else:
        print('FAIL')
print(name_list)
print(marks_list) 
print(avg_list)
#---------FOR GRACE MARKS----------------
after_grace=[]
avg_aftrgrace=[]
t=0#for rank
for e in marks_list:
        mark=[]
        p=e[0]
        c=e[1]
        m=e[2]
        if p<50 and c>=50 and m>=50:
            x=50-p 
            if(x<=10):
                p+=x
        if p>=50 and c<50 and m>=50:
            x=50-c 
            if(x<=10):
                c+=x
        if p>=50 and c>=50 and m<50:
            x=50-m
            if(x<=10):
                m+=x
        if p<50 and c<50 and m>=50:
            x=50-p
            y=50-c
            if(x+y<=10):
                p+=x
                c+=y
        if p<50 and c>=50 and m<50:
            x=50-p
            y=50-m
            if(x+y<=10):
                p+=x
                m+=y
        if p>=50 and c<50 and m<50:
            x=50-m
            y=50-c
            if(x+y<=10):
                m+=x
                c+=y
        if p<50 and c<50 and m<50:
            x=50-p
            y=50-c
            z=50-m
            if(x+y+z<=10):
                p+=x
                c+=y
                m+=z
        if p>=50 and c>=50 and m>=50:
            t=1
        new_avg=(p+c+m)/3
        mark.append(p)
        mark.append(c)
        mark.append(m)
        after_grace.append( mark)
        avg_aftrgrace.append(round(new_avg,2))
print(f'Names: {name_list}')
print(f'Marks: {after_grace}')
print(f'Average: {avg_aftrgrace}')
#------RANK----------------------------- 
print('RANK:')
#asc_avg=sorted(avg_aftrgrace)
asc_marks=sorted(after_grace)
#print(asc_avg[::-1])
i=0
j=i+1
while i<=len(avg_aftrgrace):
    while j<len(avg_aftrgrace):
        if(avg_aftrgrace[i]<avg_aftrgrace[j]): 
            temp=avg_aftrgrace[i]
            avg_aftrgrace[i]=avg_aftrgrace[j]
            avg_aftrgrace[j]=temp
            temp=name_list[i]
            name_list[i]=name_list[j]
            name_list[j]=temp
        j+=1
    i+=1
result=[]
for e in range(0,len(avg_aftrgrace)):
      if(avg_aftrgrace[e]>=50 and t==1):
          result.append('PASS')
      else:
          result.append('FAIL')
print(name_list)
print(avg_aftrgrace)
print(asc_marks[::-1])
print(result)
                

    


