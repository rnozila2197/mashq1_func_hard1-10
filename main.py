# 1-10
# 1
def son_tekshir(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return "Hammasi musbat"
    else:
        return "Manfiy mavjud"

res = son_tekshir(5, 3, 2)
print(res)

# 2
def son(a):
    if a == 1 and 9:
        return "Bir xonali"
    elif a == 10 and 99:
        return "Ikki xonali"
    else:
        "Boshqa"

res = son(10)
print(res)

# 3
def juft_toq(a, b):
    if a % 2 == 0:
        if b % 2 != 0:
            return "Turli turdagi!"
        else:
            return "Bir xil turdagi"

res = juft_toq(4)
print(res)

# 4
def matn(a):
    if len(a) % 2 == 0 and a > 6:
        return "Mos keladi"
    else:
        return "Mos emas"

# 5
def yosh_tek(a):
    if a < 18:
        return "Voyaga yetmagan!"
    elif a <= 18:
        return "Talaba"
    else:
        return "Oddiy fuqaro"

res = yosh_tek(18)
print(res)

# 6
def son(a):
    if a % 3 == 0 or a % 5 == 0:
        return "Mos son"
    else:
        return "Mos emas"

res = son(15)
print(res)

# 7
def login_tekshir(login):
    if len(login) < 5 or " " in login:
        return "Noto‘g‘ri login"
    else:
        return "To‘g‘ri login"

res = login_tekshir("ali16")
print(res)

# 8
def parol_tekshir(parol):
    if any(harf.isupper() for harf in parol) and any(harf.isdigit() for harf in parol):
        return "Kuchli parol"
    else:
        return "Kuchsiz parol"

print(parol_tekshir("Salom123"))

# 9
def son_tek(son):
    if son > 0 and son % 2 == 0:
        return "Musbat juft!"
    elif son > 0 and son % 2 != 0:
        return "Musbat toq!"
    else:
        return "Manfiy yoki emas"

res = son_tek(4)
print(res)

# 10
def matn(a, b):
    if len(a) == len(b):
        return "Uzunligi teng!"
    else:
        return "Uzunligi teng emas!"

res = matn("Jamshid", "Jemfur6")
print(res)



# 11 - 20
# 11
def gap_tekshir(matn):
    if matn[0].isupper() and matn[-1] == ".":
        return "To‘g‘ri gap"
    else:
        return "Xato format"

res = gap_tekshir("Salom dunyo.")
print(res)

# 12
def email(a):
    if a == "@" and a == ".":
        return "email togri!"
    else:
        return "email notogri!"

res = email("jemfur696@gmail.com")
print(res)

# 13
def ism(a):
    if len(a) < 3:
        return "Juda qisqa"
    elif len(a) > 3 and 10:
        return "Normal"
    else:
        return "Juda uzun"

res = ism("jamshid")
print(res)

# 14
def son_tek(son):
    if son > 100 and son % 2 == 0:
        return "Katta juft"
    else:
        return "Ortiqcha belgilar bor"

res = son_tek(110)
print(res)

# 15
def matn_tekshir(matn):
    if all(harf.isalpha() or harf == " " for harf in matn):
        return "Toza matn"
    else:
        return "Ortiqcha belgilar bor"


matn = input("Matn kiriting: ")
print(matn_tekshir(matn))
