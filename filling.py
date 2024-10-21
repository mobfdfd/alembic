from datetime import datetime

from db import Provider, Supply, Customer, Employees, Goods, Orders, Session


# заполняем данными таблицы
def filling():
    # используем сессию  для взаимодействия с бд (вставлять, получать, обновлять и удалять данные)
    with Session() as session:
        # Пример данных для таблицы Provider
        providers = [
            Provider(provider_name=f"Provider {i}", provider_representative=f"Rep {i}", appeal=f"Appeal {i}",
                     contact_number=f"123456789{i}", address=f"Address {i}")
            for i in range(1, 6)
        ]
        session.add_all(providers)
        # Фиксируем изменения
        session.commit()

        # Пример данных для таблицы Supply
        supplies = [
            Supply(id_provider=i, date=datetime.now())
            for i in range(1, 6)
        ]
        session.add_all(supplies)
        session.commit()

        # Пример данных для таблицы Goods
        goods = [
            Goods(id_supply=i, name=f"Goods {i}", specifications=f"Spec {i}", description=f"Desc {i}",
                  image=f"img{i}.jpg", price_buy=10.0 * i, availability=100 * i, quantity=10 * i, price_sell=15.0 * i)
            for i in range(1, 6)
        ]
        session.add_all(goods)
        session.commit()

        # Пример данных для таблицы Customer
        customers = [
            Customer(name_full=f"Customer {i}", address=f"Customer Address {i}", phone=f"111111111{i}")
            for i in range(1, 6)
        ]
        session.add_all(customers)

        # Пример данных для таблицы Employees
        employees = [
            Employees(name_last=f"Last{i}", name_first=f"First{i}", name_middle=f"Middle{i}",
                      occupation=f"Occupation {i}", address=f"Employee Address {i}", phone=f"222222222{i}",
                      date_birth=datetime(1980 + i, 1, 1))
            for i in range(1, 6)
        ]
        session.add_all(employees)
        session.commit()

        # Пример данных для таблицы Orders
        orders = [
            Orders(id_employee=i, id_good=i, date_placement=datetime.now(), date_execution=datetime.now(), id_client=i)
            for i in range(1, 6)
        ]
        session.add_all(orders)
        session.commit()


filling()
