Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input()
out = ""
for i in range(1,len(name)+1):
    letter = name[i-1]
    if (len(out)>0):
        if (letter != out[len(out)-1]):
            out+= letter
    else:
        out += letter
print(out)
