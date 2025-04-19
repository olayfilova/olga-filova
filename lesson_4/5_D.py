# DEPENDENCY INVERSION
from abc import ABC, abstractmethod


class DBDriver(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def save_data(self):
        raise NotImplementedError

    def insert_data(self):
        pass


class PostgresDriver(DBDriver):
    def connect(self):
        print("Connecting to Postgres")

    def save_data(self):
        ...


class MySQLDriver(DBDriver):
    def connect(self):
        print("Connecting to MySQL")

    def save_data(self):
        ...


class NewServer:
    def __init__(self, db: DBDriver):
        self.db = db

    def start(self):
        self.db.connect()

    def insert_data(self):
        self.db.insert_data()
        ...


