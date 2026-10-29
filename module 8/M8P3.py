# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:22:59 2026

@author: shama
"""

total_bonus = 0.0

file = open("employees.txt", "r")
name = file.readline().strip()

while name != "":
    salary = float(file.readline().strip())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus += bonus
    print(f"{name:<12}Salary: ${salary:>11,.2f}   Bonus: ${bonus:>10,.2f}")

    name = file.readline().strip()

file.close()

print()
print(f"Total bonuses paid: ${total_bonus:,.2f}")