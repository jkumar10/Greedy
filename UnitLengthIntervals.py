#A=[0.2,0.2,1.5,1,2.2,2.3,4,3,1.2,0.7,0.8,6,9,10,100,101,105,110]
A=[0.7,1.0,1.5,2.0,2.3,2.6,3.1,3.6,3.9,4.2,4.7,5.2,5.5]
A.sort()
B=A
print B
S=[]
start_interval=B[0]
end_interval=start_interval+1
S.append([start_interval,end_interval])
for element in B:
    if element>end_interval:
        start_interval=element
        end_interval=start_interval+1
        S.append([start_interval,end_interval])

print S