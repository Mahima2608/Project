import pandas as pd
import psycopg2

df = pd.read_csv("products.csv")


conn = psycopg2.connect(
    host "localhost",
    database="ecommerce",
    user="postgres",
    password="root",
    port="5432"

)
cur = conn.cursor()

cur.execute("DELETE FROM products")

for _,row in df.interrows():
    cur.execute("""
                    INSERT INTO products (product_id,name, category,price,stock,rating)
                VALUES (%s, %s,%s,%s,%s,%s)
                ON CONFLICT(product_id) DO NOTHING;
                """,(
                    row['product_id'],
                    row['name']
                    row['category']
                    row['price']
                    row['stock']
                    row['rating']
                ))
conn.commit()
cur.close()
conn.close()    