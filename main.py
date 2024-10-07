x= {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
F=int(input("Enter the value you want to see the frequency"))
print("The original Values are",x)
g=F
count=0
for key in x:
    if x[key]==g:
        count=count+1
print("Frequency of value is:",count)        


