from ftplib import print_line

# arr = [1, 5, 10, 14, 20, 6, 8, 10]
# for i, num in enumerate(arr):
#     print(f"i - {i}, num - {num}")
#
# row = ""
# for i, num in enumerate(arr):
#     row += f"{i}/{num} zhopa, "
# print_line(f"{row}")

# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.
# print("========1=========")
# def suma(sk_1, sk_2):
#     suma = sk_1 + sk_2
#     print_line(suma)

# suma(1, 2)

# print("========2=========")
# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

# def PISq(daugiklis):
#     num = 9.8596 * daugiklis
#     return num

# PISq(2)
# print("-----------------------------------------------------------------")
# num2 = suma(9999999, 55555555555)
# print("==================")
# print("-----------------------------------------------------------------")
# print(num2)
#
# print("-----3-----")
# S?ukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.

# def multiply(a, b):
#     print(a * b)
#
# multiply(5, 3)

# print("========4=========")
# # Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
#
# def print_array(arr):
#     for item in arr:
#         print(item, end=" ")
# print_array([1, 2, 3, 4, 5])


# print("=========5=========")
# # Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.
#
import random
# def random_int(min_val, max_val):
#     return random.randint(min_val, max_val)
#
# print(random_int(10, 50))

# print("=========6=========")
# Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.
# def random_int_array(min_val, max_val, length):
#     return [random.randint(min_val, max_val) for _ in range(length)]
#
# print(random_int_array(10, 50, 5))

#
# print("=========7=========")
# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.

# def sum_array(arr):
#     return sum(arr)
#
# random_numbers = [23, 45, 12, 38, 50]
# print(sum_array(random_numbers))

# print("=========8=========")
# # Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
# def generuoti_atsitiktiniu_skaiciu_masyva(min_reiksme, max_reiksme, ilgis):
#     return [random.randint(min_reiksme, max_reiksme) for _ in range(ilgis)]
#
# min_reiksme = 1
# max_reiksme = 100
# ilgis = 20
#
# atsitiktiniu_skaiciu_masyvas = generuoti_atsitiktiniu_skaiciu_masyva(min_reiksme, max_reiksme, ilgis)
# print(atsitiktiniu_skaiciu_masyvas)

print("=========9=========")
# Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.

# def atspausdinti_staciakampi(eiluciu_skaicius, stulpeliu_skaicius):
#     for _ in range(eiluciu_skaicius):
#         for _ in range(stulpeliu_skaicius):
#             print("*", end="")
#         print()
# eiluciu_skaicius = 5
# stulpeliu_skaicius = 10
# atspausdinti_staciakampi(eiluciu_skaicius, stulpeliu_skaicius)

print("=========10=========")

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)

# from collections import Counter
#
# def analizuoti_sakinį(sakinys):
#     skaiciavimai = Counter(sakinys)
#     raidziu_skaicius = sum(skaiciavimai[raide] for raide in skaiciavimai if raide.isalpha())
#     tarpu_skaicius = skaiciavimai[" "]  # Tarpo simbolis yra " "
#
#     print(f"Simbolių (raidžių) skaičius: {raidziu_skaicius}")
#     print(f"Tarpų skaičius: {tarpu_skaicius}")
#
# # Pavyzdys, kaip naudoti funkciją
# sakinys = "Šiandien labai graži diena"
# analizuoti_sakinį(sakinys)
#
# sakinys2 = "Labas, pasauli! 123"
# analizuoti_sakinį(sakinys2)















