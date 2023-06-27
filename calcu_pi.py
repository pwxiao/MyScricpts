i = 0
pi = 0
while True:
    if i%2==0:
        pi+=1/(2*i+1)
    else:
        pi-=1/(2*i+1)
    i=i+1;
    print(4*pi)
        
