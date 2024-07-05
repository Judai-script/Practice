def Exalt(x):
    match x:
        case 1:
            print("Exalt the machine spirit!!!")
        case 2:
            print("Exalt the god emperor!!!")
        case 3:
            print("Exalt the Code Astartes!!!")
Exalt(1)
try:
    x=input("Hail citizen! What will you be exalting today? ")
    Exalt(x)
except ValueError:
    print("input ONLY 1,2 or 3. or else you may offend the machine spirit")
except TypeError:
    print("input ONLY numbers. other data type may offend the machine spirit!")
except Exception:
    print("MACHINE SPIRIT OFFENDED!!! CONTACT A CERTIFIED TECH PRIEST IMMEDIATELY!!!")
else:
    print("wise choice citizen. Glory to the empire!")
finally:
    print("shalalalallallalala shalalalallallalala")