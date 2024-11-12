import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
symbols = "`!@#$%^&*()_+{}\"';:\|<>?/"
numbers = "1234567890"

application = input("What application/website is this for: ")
length = input("How long would you like the password: ")


combine = upper + lower + symbols + numbers 

out = "".join(random.sample(combine, int(length)))
print(application,": " + out)

input("press Enter to exit...")
