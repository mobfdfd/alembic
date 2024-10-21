from sqlalchemy.engine import URL

drivername = "postgresql"
username = "postgres"
host = "localhost"
database = "stoke"
password = "postgres"

# настройки подключения к базе данных
class Settings():
    @classmethod
    def url_create(cls):
        # создаем url
        url = URL.create(drivername=drivername, username=username, host=host, database=database, password=password)
        return url

print(Settings.url_create())