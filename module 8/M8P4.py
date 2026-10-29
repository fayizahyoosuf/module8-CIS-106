# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:25:52 2026

@author: shama
"""

total = 0.0
order_count = 0

file = open("orders.txt", "r")
item = file.readline().strip()

while item != "":
    quantity = int(file.readline().strip())
    price = float(file.readline().strip())

    extended = quantity * price
    total += extended
    order_count += 1

    print(f"{item:<10}Qty: {quantity:>4}   Price: ${price:>8,.2f}   Extended: ${extended:>10,.2f}")

    item = file.readline().strip()

file.close()

print()
print(f"Sum of extended prices: ${total:,.2f}")
print(f"Number of orders: {order_count}")
if order_count > 0:
    print(f"Average order: ${total / order_count:,.2f}")