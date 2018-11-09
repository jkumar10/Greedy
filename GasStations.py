D=[5,10,12,13,14,15,20,21,22,23,24,25]
m=4
S=[]
preious_GS_stop=0
i=1
while i<=len(D)-1:
    if m<(D[i]-preious_GS_stop):
        stop_position=D[i-1]
        S.append(stop_position)
        preious_GS_stop=stop_position
    i=i+1


print S