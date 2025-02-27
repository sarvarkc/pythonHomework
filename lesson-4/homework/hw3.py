txt = input("Enter a string: ")

txt_list = []
letters_list = []
vowels = ['a', 'e', 'i', 'o', 'u']


for i in range(len(txt)):
    if txt[i] in vowels:
       txt_list.append(txt[i])
    elif i+1 == len(txt):
        txt_list.append(txt[i])
    elif (i+1) % 3 == 0:
        if txt[i] in letters_list:
            txt_list.append(txt[i])
        else:
            txt_list.append(txt[i])
            txt_list.append("_")
            letters_list.append(txt[i])
    else:
        txt_list.append(txt[i])

print("".join(txt_list))

