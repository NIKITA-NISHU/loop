n=int(input("enter the number="))
reverse=0
while n>0:
    reverse=(reverse*10)+n%10
    n=n//10
print(reverse)

# num=int(input("enter the number="))
# n=str(num)
# i=1
# s=" "
# while i<=len(n):
#     a=n[-i]
#     s=s+a
#     i+=1
# print(int(s))
