import sqlite3

conn = sqlite3.connect("data.sqlite")

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE empanadas (Cliente VARCHAR(20), CC INT, CJyQ INT, CH INT, Precio FLOAT)")
except:
    print("No se pudo crear la tabla")

conn.close()
