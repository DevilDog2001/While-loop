#1
for a in range(0,151):
    print(a)
#2
for b in range(5,1001,5):
    print(b) 
#3
for c in range(1,101):
    if c % 5 == 0 and c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)
#4
def oddsums(n):
    
    s_um = 0
    for d in range(0,n):
        if d % 2 == 1:
            s_um += d
    return s_um
        
print(oddsums(500_001))
#5
e = 2018
while e > 0:
    print(e)
    e -= 4
else:
    print("Done")
#6
lowNum = 2 
highNum = 9
mult = 3 
for z in range(lowNum,highNum,mult):
    print(z+1, end = " ")