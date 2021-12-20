alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(string, key):
    arr = []

    for x in string:
        if x != " ":
            arr.append(alphabets[(alphabets.index(x) + key)%26])

        else:
            arr.append(" ")

    for y in arr:
        print(y, end= "")

def decrypt(string, key):
    arr = []

    for x in string:
        if x != " ":
            arr.append(alphabets[(alphabets.index(x) - key)%26])
        else:
            arr.append(" ")
    
    for y in arr:
        print(y, end = "")


e_mess = input("Enter Anything in small caps(encrypted): ")
shift_key = int(input("Enter Key: "))

decrypt(e_mess, shift_key)
print("\n")

d_mess = input("Enter Anything in small caps(decrypted): ")
shift_key = int(input("Enter Key: "))

encrypt(d_mess, shift_key)
print("IQRAAAAAAAA")
print("\n")
