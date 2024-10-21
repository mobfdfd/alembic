from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, NUMERIC, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import Settings

# создаем движок - объект Engine
engine = create_engine(Settings.url_create())

# подключение к базе данных
connection = engine.connect()
# создаем базовую модель, от которой потом наследуются остальные модели
Base = declarative_base()

# определяем модели (таблицы)
class Provider(Base):
    __tablename__ = 'providers'

    id = Column(Integer(), nullable=False, primary_key=True)
    provider_name = Column(String(100), nullable=True)
    provider_representative = Column(String(100), nullable=True)
    appeal = Column(String(100), nullable=True)
    contact_number = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)


class Supply(Base):
    __tablename__ = "supply"

    id = Column(Integer(), primary_key=True)
    id_provider = Column(Integer(), ForeignKey("providers.id"))
    date = Column(DateTime(), default=datetime.now)


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer(), primary_key=True)
    name_full = Column(String(64))
    address = Column(String(128))
    phone = Column(String(16))


class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer(), primary_key=True)
    name_last = Column(String(16))
    name_first = Column(String(16))
    name_middle = Column(String(16))
    occupation = Column(String(32))
    address = Column(String(128))
    phone = Column(String(16))
    date_birth = Column(String(100))


class Goods(Base):
    __tablename__ = "goods"

    id = Column(Integer(), primary_key=True)
    id_supply = Column(Integer(), ForeignKey("providers.id"))
    name = Column(String(32))
    specifications = Column(Text())
    description = Column(Text())
    image = Column(String(128))
    price_buy = Column(NUMERIC())
    availability = Column(Integer())
    quantity = Column(Integer())
    price_sell = Column(NUMERIC())


class Orders(Base):
    __tablename__ = "orders"

    id_order = Column(Integer(), primary_key=True)
    id_employee = Column(Integer(), ForeignKey("employees.id"))
    id_good = Column(Integer(), ForeignKey("goods.id"))
    date_placement = Column(DateTime(), default=datetime.now)
    date_execution = Column(DateTime(), default=datetime.now)
    id_client = Column(Integer(), ForeignKey("customer.id"))


# создаем таблицы, которые определили выше, в бд
Base.metadata.create_all(engine)

# создаем класс сессии
Session = sessionmaker(bind=engine)