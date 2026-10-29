# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:08:35 2026

@author: shama
"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

initial_principal = principal
total_interest_earned = 0

print(f"\n{'Year':<5}{'Beginning':<18}{'Ending'}")
print(f"{'':<5}{'Balance':<18}{'Balance'}")

for year in range(1, 6):
    interest = principal * rate
    ending_balance = principal + interest
    total_interest_earned += interest
    
    print(f"{year:<5}${principal:,.2f}{'':<8}${ending_balance:,.2f}")
    principal = ending_balance

print(f"\nTotal interest earned: ${total_interest_earned:,.2f}")