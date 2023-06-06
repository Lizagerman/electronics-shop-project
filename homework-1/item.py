class Item:
    pass

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.name = "Смартфон"
    item1.price = 10000
    item1.quantity = 20


    item2.name = "Ноутбук"
    item2.price = 20000
    item2.quantity = 5



    print(item1.calculate_total_price(item1.price*item1.quantity))
    print(item2.calculate_total_price(item2.price*item2.quantity))

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount(item1.price * Item.pay_rate)
    item2.apply_discount(item2.price * Item.pay_rate)

    print(item1.price)
    print(item2.price)

    print(Item.all)

