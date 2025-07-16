import os
from dotenv import load_dotenv
from database import DataBase, Data
from sqlalchemy.orm import sessionmaker
from datetime import date


db = DataBase("mysql",os.getenv("sql_user"),os.getenv("sql_pass"),db_name="Orders_Python")
engine = db.engine()

Session = sessionmaker(bind=engine)
with Session() as session:
    
    sample_orders = [
        Data(Id=1, date=date(2025, 7, 1), product="Laptop", order_value=1200, status="shipped"),
        Data(Id=2, date=date(2025, 7, 2), product="Smartphone", order_value=800, status="delivered"),
        Data(Id=3, date=date(2025, 7, 3), product="Headphones", order_value=150, status="pending"),
        Data(Id=4, date=date(2025, 7, 4), product="Monitor", order_value=300, status="shipped"),
        Data(Id=5, date=date(2025, 7, 5), product="Keyboard", order_value=70, status="cancelled"),
        Data(Id=6, date=date(2025, 7, 6), product="Mouse", order_value=40, status="delivered"),
        Data(Id=7, date=date(2025, 7, 7), product="Printer", order_value=200, status="shipped"),
        Data(Id=8, date=date(2025, 7, 8), product="Tablet", order_value=500, status="pending"),
        Data(Id=9, date=date(2025, 7, 9), product="Webcam", order_value=90, status="delivered"),
        Data(Id=10, date=date(2025, 7, 10), product="External Drive", order_value=110, status="shipped"),
    ]
    session.add_all(sample_orders)
    session.commit()
    print("Sample orders inserted successfully.")
