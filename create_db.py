import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cur.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price INTEGER
)
""")

cur.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT
)
""")

cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", [
    (1, "Ali", "Tehran"),
    (2, "Sara", "Shiraz"),
    (3, "Reza", "Tehran"),
    (4, "Mina", "Isfahan"),
])

cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", [
    (1, "Laptop", "Electronics", 25000),
    (2, "Headphones", "Electronics", 2000),
    (3, "Desk", "Furniture", 5000),
    (4, "Chair", "Furniture", 3500),
])

cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 1, 1, "2026-10-01"),
    (2, 2, 2, 2, "2026-10-03"),
    (3, 3, 3, 1, "2026-10-05"),
    (4, 1, 4, 2, "2026-10-07"),
    (5, 4, 1, 1, "2026-10-09"),
])





conn.commit()
conn.close()
print("Database created!")