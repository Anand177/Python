from datetime import datetime, timedelta
from faker import Faker

import pandas as pd
import random

faker = Faker()
num_rows = 100

order_ids = [1000 + i for i in range(num_rows) ]
customer_names = [faker.name() for _ in range(num_rows)]
order_quantity = [random.randint(1,10) for _ in range(num_rows)]

products = [
    ('Laptop', 60000), ('Smartphone', 30000), ('Headphones', 2000), ('Smartwatch', 5000), 
    ('Tablet', 20000), ('Monitor', 5000), ('Keyboard', 1500), ('VR Headset', 12000), 
    ('USB Drive', 9000), ('Printer', 13000), ('Gaming Console', 50000), ('Mouse', 300)
]
product_name : list[str] = []
order_value: list[int] = []

for i in range(num_rows):
    product = products[random.randint(0,11)]
    product_name.append(product[0])
    order_value.append(product[1] * order_quantity[i])

start_date = datetime(2025, 1, 1)
order_date = []
for _ in range(num_rows):
    # Generate a random number of days from start_date
    random_days = random.randint(1, 365 * 2) # Up to 2 years after start_date
    order_date.append((start_date + timedelta(days=random_days)).strftime('%Y-%m-%d'))

shipped_status = [random.choice(['Yes', 'No']) for _ in range(num_rows) ]

country_codes = [
    'USA', 'CAN', 'GBR', 'DEU', 'FRA', 'JPN', 'AUS', 'CHN', 'IND', 'BRA',
    'MEX', 'ESP', 'ITA', 'KOR', 'RUS', 'ARG', 'NLD', 'SWE', 'CHE', 'SGP'
]
country = [random.choice(country_codes) for _ in range(num_rows)]

data = {
    "OrderId" : order_ids,
    "CustomerName" : customer_names,
    "ProductName" : product_name,
    "OrderQuantity" : order_quantity,
    "OrderValue" : order_value,
    "OrderDate" : order_date,
    "ShippedStatus" : shipped_status,
    "Country" : country
}

df = pd.DataFrame(data)
df.to_csv("Data/synthetic_order.csv", index=False)