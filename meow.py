import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Time
)

# Using ORM to do Bulk operation
credentials = {
    'username': 'Internship01',
    'password': '1234',
    'host': 'localhost',
    'database': 'MRO',
    'port': '1433'}

connect_url = sqlalchemy.engine.url.URL(
    'mssql+pyodbc',
    username=credentials['username'],
    password=credentials['password'],
    host=credentials['host'],
    port=credentials['port'],
    database=credentials['database'],
    query=dict(driver='SQL+Server', echo='True')
)

engine = create_engine(connect_url)
a = []
with open("book1.prn", "r") as file:
    for line in file:
        a.append(" ".join(line.split()))


class Table(Base):
    __tablename__ = ''
    id = Column(String)
    time = Column(Time)
    v0 = Column(Float)
    v1 = Column(Float)
    v2 = Column(Float)
    v3 = Column(Float)
    v4 = Column(Float)
    v5 = Column(Float)
    v6 = Column(Float)
    v7 = Column(Float)
    v8 = Column(Float)
    v9 = Column(Float)
    v10 = Column(Float)
    v11 = Column(Float)
