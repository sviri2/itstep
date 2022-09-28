str = input("შეიყვანე ძველი მაკი: ")
res_str = str.replace(' ', '') 
res_str = res_str[:4] + "." + res_str[4:]
res_str = res_str[:9] + "." + res_str[9:]

if str[2] == " " and str[2] == ":" :
    print("არასწორი ფორმატი")

else:

    
    new_mac = ("თქვენი ახალი  მაკი: {}")
    print(new_mac.format(res_str))

