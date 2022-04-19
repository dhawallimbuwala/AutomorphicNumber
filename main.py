print ("Enter any number to check:::")
n = int(input())

d = len(str(n))

output = ((n**2 - n) % 10**d)

print(output)

if output == 0:
    print("ohh!! yeah,, you entered the Automorphic number")
else:
    print("Please enter another number.")
