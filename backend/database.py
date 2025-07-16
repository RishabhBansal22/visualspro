from sqlalchemy import create_engine, Integer, String, Column, Date
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os


load_dotenv()
Base = declarative_base()
class Data(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    product = Column(String(255))


class DataBase:
    def __init__(self, db_server:str, user, password, host:str="localhost", port:int=3306, db_name: str= None):
        self.server = db_server.lower()
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = db_name
    
    server_driver = {
        "mysql" : "pymysql",
        "postgres" : "psycopg2"
         
     }
    
    def engine(self):
        driver = DataBase.server_driver.get(self.server)
        if not driver:
            raise ValueError(f"Unsupported server: {self.server}")
        dialect = "mysql" if self.server == "mysql" else "postgresql"
        url = f"{dialect}+{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        try:
            engine = create_engine(url=url)
            Base.metadata.create_all(engine)
            print("succesfully connected with engine\nDataBase created successfully")
            return engine
        except Exception as e:
            return f"could not connect with engine {e}"
            

db = DataBase("mysql",os.getenv("sql_user"),os.getenv("sql_pass"),db_name="Orders_Python")
engine = db.engine()
print(engine)
        












