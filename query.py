from sqlalchemy import func

from db import Provider, Employees, Goods, Orders, Supply, Session

with Session() as session:
    # Получаем данные из таблицы и выводим на экран
    print("---------------Задание 5---------------")
    providers = session.query(Provider).all()
    for provider in providers:
        print(provider.id, provider.provider_name, provider.provider_representative, provider.appeal, provider.address,
              provider.contact_number)

    print("---------------Задание 6---------------")
    result = session.query(Supply, Provider).join(Provider, Supply.id_provider == Provider.id)
    for r1, r2 in result:
        print(r1.id, r2.provider_name)

    print("---------------Задание 7---------------")
    order1 = session.query(Orders).filter_by(id_order=1)
    order1.id_good = 4
    session.commit()
    print(order1.id_good)

    print("---------------Задание 8.1---------------")
    goods = session.query(Goods, Orders).join(Orders, Orders.id_good == Goods.id).where(Goods.price_buy > 20)
    for good, order in goods:
        print(order.id_good, good.price_buy)

    print("---------------Задание 8.2---------------")
    goods2 = session.query(Goods).order_by(Goods.price_buy)
    for good in goods2:
        print(good.id, good.price_buy)

    print("---------------Задание 8.3---------------")
    goods2 = session.query(Goods.price_buy, func.count(Goods.id)).group_by(Goods.price_buy)
    for price_buy, count in goods2:
        print(price_buy, count)

    print("---------------Задание 8.4---------------")
    employees = session.query(Employees, Orders).join(Orders, Orders.id_employee >= 5).distinct(Orders.id_order)
    for employee, order in employees:
        print(order.id_employee, order.id_order)

    print("---------------Задание 9.1---------------")
    goods3 = session.query(Goods, Orders).join(Orders, Orders.id_good == Goods.id)
    count = goods3.count()
    print(count)

    print("---------------Задание 9.2---------------")
    # Подсчет количества записей в таблице Goods
    count1 = session.query(func.count(Goods.id)).scalar()
    print("Total number of goods:", count1)

    print("---------------Задание 9.3---------------")
    # Подсчет среднего значения столбца price_buy
    avg_price = session.query(func.avg(Goods.price_buy)).scalar()
    print("Average price of goods:", avg_price)

    print("---------------Задание 9.4---------------")
    # Максимальное и минимальное значения столбца price_buy
    max_price = session.query(func.max(Goods.price_buy)).scalar()
    min_price = session.query(func.min(Goods.price_buy)).scalar()
    print("Maximum price of goods:", max_price)
    print("Minimum price of goods:", min_price)

    print("---------------Задание 10---------------")
    new_provider = Provider(provider_name='Новый поставщик', address='Новый адрес')
    session.add(new_provider)
    session.commit()
    providers2 = session.query(Provider).all()
    for prov in providers2:
        print(prov.provider_name)
    print("---------------После удаления---------------")
    session.query(Provider).where(Provider.provider_name == 'Новый поставщик').delete()
    session.commit()
    providers3 = session.query(Provider).all()
    for prov in providers3:
        print(prov.provider_name)
