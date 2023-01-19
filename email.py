email = input("Enter your Email") #g@G.com , khalidhusain00112@gmail.com
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1 
                if k == 1 or j == 1 or d == 1:
                    print("wrong Email (there should not be any space in the email)")
                else:
                    print("you got the right email")
            else:
                print("wrong Email( . is wrongly used either it is not prescribed position or it is used multiple times)")
        else:
            print("wrong Email (either @ is not present in email or @is used more than once)")
    else:
        print("wrong Email(first position is not an alphabet)")
else:
    print("wrong Email 1(email less than 6 letters)")
