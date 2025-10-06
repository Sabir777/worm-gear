#!/usr/bin/env python3

n = 1413 # Обороты в минуту

# Подшипник: данные
Cr = 90000
e = 0.296
Y = 2.026
X = 0.4

V = 1
Kb = 1.3
Kt = 1
p = 10/3

# ----------Силы----------
#
#        (Fa)--->
#   (A)--->     <---(B)
#
# Силы от подшипников и осевая сила
# направлены как на рисунке: Vab == True
#
# Если сила Fa направлена в другую сторону
# Установить флаг Vab == false или указать
# силу со знаком минус

Vab = True

# Силы: указывать в Ньютонах
Fa = 2890
Ra1 = 276
Ra2 = 232
Rb1 = 775
Rb2 = 233


print("Входные данные")
print("\nСилы:")
print(f"Fa = {Fa}")
print(f"Ra1 = {Ra1}")
print(f"Ra2 = {Ra2}")
print(f"Rb1 = {Rb1}")
print(f"Rb2 = {Rb2}")
print("\nПодшипник:")
print(f"Cr = {Cr}")
print(f"e = {e}")
print(f"X = {X}")
print(f"Y = {Y}")
print("\nПостоянные:")
print(f"p = {p:.3f}")
print(f"V = {V}")
print(f"Kb = {Kb}")
print(f"Kt = {Kt}")


if Fa < 0:
    Vab = false
    Fa = -Fa

Ra = (Ra1 ** 2 + Ra2 ** 2) ** 0.5
Rb = (Rb1 ** 2 + Rb2 ** 2) ** 0.5

S1 = 0.83 * e * Ra
S2 = 0.83 * e * Rb
F1, F2 = (S2, Fa + S1) if Vab else (Fa + S2, S1)
f_ek = lambda r, a: (X*V*r + Y*a)*Kb*Kt
F1_ek = f_ek(Ra, F1)
F2_ek = f_ek(Rb, F2)

print("\nВыходные данные")
print(f"Fa = {Fa}")
print(f"Ra = {Ra:.1f}")
print(f"Rb = {Rb:.1f}")
print(f"S1 = {S1:.1f}")
print(f"S2 = {S2:.1f}")
print(f"F1 = {F1:.1f}")
print(f"F2 = {F2:.1f}")
print(f"F1_ek = {F1_ek:.1f}")
print(f"F2_ek = {F2_ek:.1f}")

f_l = lambda x: (Cr/x) ** p
L1 = f_l(F1_ek)
L2 = f_l(F2_ek)

print(f"Срок службы 1-го подшипника = {L1:.0f} млн.об")
print(f"Срок службы 2-го подшипника = {L2:.0f} млн.об")

f_lh = lambda x: 1e6 * x / (60 * n)
lh1 = f_lh(L1)
lh2 = f_lh(L2)

print(f"Срок службы 1-го подшипника = {lh1:.0f} часов")
print(f"Срок службы 2-го подшипника = {lh2:.0f} часов")

