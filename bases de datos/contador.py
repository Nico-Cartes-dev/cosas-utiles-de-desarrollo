# importa tu base de datos
# import db
import sqlite3

# Initialize DB connection (assuming db.py has a connection or we can use sqlite3 directly)
# Checking db.py content via previous analysis... it uses 'taller.db' or similar?
# Let's just use the db module since it's there.
tabla="pon como se llame la tabla"
# conn = db.conectar_db()
cursor = conn.cursor()
cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
total = cursor.fetchone()[0]
print(f"Total orders: {total}")

cursor.execute(f"SELECT estado, COUNT(*) FROM {tabla} GROUP BY estado")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]}: {row[1]}")

conn.close()