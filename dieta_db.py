import sqlite3

DATABASE_NAME = "dieta.db"
#importo y me conecto

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

#creo la tabla
#recorro la lista de tablas, hay una sola
def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS dieta(
                id  PRIMARY KEY,
                restriction TEXT NOT NULL,
                restriccion TEXT NOT NULL,
                usd REAL NOT NULL
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
#le agrego los datos que me da el ejercicio
def insert_initial_data():
    data = [
        ("R001", "Gluten-free", "Libre de Gluten", 100),
        ("R002", "Dairy-free", "Libre de Lácteos", 112),
        ("R003", "Nut-free", "Libre de Frutos Secos", 123),
        ("R004", "Vegetarian", "Vegetariano", 144),
        ("R005", "Vegan", "Vegano", 155)
    ]
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dieta'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # La tabla "dieta" no existe, proceder con la inserción de datos
        cursor.executemany("INSERT INTO dieta (id, restriction, restriccion, usd) VALUES (?, ?, ?, ?)", data)


    db.commit()



create_tables()
insert_initial_data()
