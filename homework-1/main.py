from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.name = "Смартфон"
    item1.price = 10000
    item1.quantity = 20

    item2.name = "Ноутбук"
    item2.price = 20000
    item2.quantity = 5


    print(item1.calculate_total_price())
    print(item2.calculate_total_price())

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)
    print(item2.price)

    print(Item.all)

