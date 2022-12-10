f = open("text.txt",'r')
contents =f.read()
print(contents)
f.close()

try:
    f = open("DoesNotExist.file",'r')
except FileNotFoundError as error:
    print("you should check that \'DoesNotExist.file\'")
