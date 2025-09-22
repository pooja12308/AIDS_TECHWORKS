<<<<<<< HEAD
#program to print highest frequency & lowest frequency character in a string

def max_freq(str):
    freq={}
    for ch in str:
        if ch==" ":
            break
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    for i in freq:
        if(max(freq[i])):
            print()

=======
#program to print highest frequency & lowest frequency character in a string

def max_freq(str):
    freq={}
    for ch in str:
        if ch==" ":
            break
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    for i in freq:
        if(max(freq[i])):
            print()

>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
            -------------