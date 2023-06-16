start=int(input("Enter the starting number of the range: "))
end=int(input("Enter the ending number of the range: "))
print("Positive numbers in the range are:")
for n in range(start,end+1):
    if n>0:
        print(n)