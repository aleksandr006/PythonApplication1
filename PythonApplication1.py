from module1 import *
while True:
    print("funksioind".center(50,"+"))
    print("arithmetic- A,\nis_year_leap-Y")
    v=input("arithmetic- A")
    if v.upper()=="A":
        a=float(input("esimene arv"))
        b=float(input("teine arv"))
        sym=input("Tehe:")
        rezult=arithmetic(a,b,sym)
        print(rezult)
    elif v.upper()=="Y":
        is_year_leap()
        rezolut=is_year_leap((int(input("sisesta aasta"))))
 