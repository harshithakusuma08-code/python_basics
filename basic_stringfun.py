print("HELLO WORLD!!")
message="I'm HARSHITHA and I am from ANDHRA PRADESH"
print(message)
print("length of the string:",len(message))
print(message[0])
print(message[0:10])
print(message[len(message)-1])
print(message[0:len(message)-1])
print(message[0:len(message)])
print(message[0:len(message)//2])
print(message[len(message):0])
"""--it doesn't work because for the code we given
starting point as length and ending point as 0 and we didn't given the increasing
or decreasing step so the compiler thinks that +1 to be increased in so from the
given input we come to know that start from ending index and increase by one
as it is the last value we can't go further. Hence it returns 'empty string'"""
#slicing
print(message[4:])
print(message[:10])
print(message[len(message)//2:])
print(message[:len(message)//2])
print(message[:len(message)//2:-1])
print(message[::-1])
print(message[len(message)::-1])
print(message[len(message)//2::-1])
#string functions
name="naruto uzumaki"
name=name.replace("uzumaki","namikaze")
print(name)
name="naruto uzumaki"
print(name.upper())
print(name.lower())
print(name.find("a"))
#print(name.find(len(name)))#argument must be a string
print(name.find("uzumaki"))
print(name.find(name[0:len(name)//2]))
print(name.find("u"))
print(name.count("a"))
#print(name.count(name.find("a")))#argument must be string
print(name.count("uzumaki"))
print(name.count("u"))
print(name.replace("uzumaki","namikaze"))
new_name=name.replace("uzumaki","namikaze")
print(new_name)
her_name="hinata hyuga"
new_name=name+" "+her_name
print(new_name)
print(name+" "+her_name)
new_name="{} {} are husband and wife".format(name,her_name)
print(new_name)
new_name=f"{name} {her_name} are husband and wife"
print(new_name)

