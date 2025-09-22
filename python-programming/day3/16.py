<<<<<<< HEAD
#input:aaabbca output:a4b2c1

def count_occur(str):
    freq={}
    for i in str:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    res=""
    for i in freq:
        res+=f"{i}{freq[i]}"
    print(res)
str=input("Enter a string")
count_occur(str)




def compress_string(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result
s = "aaabbca"
print("Input:", s)
print("Output:", compress_string(s))
=======
#input:aaabbca output:a4b2c1

def count_occur(str):
    freq={}
    for i in str:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    res=""
    for i in freq:
        res+=f"{i}{freq[i]}"
    print(res)
str=input("Enter a string")
count_occur(str)




def compress_string(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result
s = "aaabbca"
print("Input:", s)
print("Output:", compress_string(s))
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
