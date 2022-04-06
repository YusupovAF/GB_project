
item_number = 3
total_price = 0
while item_number > 0:
    shop_item = float(input('Insert item cost: '))
    total_price += shop_item
    item_number -= 1
print(shop_item, total_price)