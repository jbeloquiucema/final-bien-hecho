from copa_db import get_db
from class_copa import Copa

#hago la funcion para insertar copas faltantes
def insert_copa(id, estadio, partido, precio, sector):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO copa (id, estadio, partido, precio, sector) \
    VALUES ( ?, ?, ?, ?, ? )"
    cursor.execute(statement, [id, estadio, partido, precio, sector])
    db.commit()
    return True

#esta funcion no la pide, pero puede llegar a ser util, si se desean actualizar los precios de las copas
def update_copa(id, estadio, partido, precio, sector):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE copa SET id = ?, estadio = ?, partido= ?, precio= ?, sector=? \
    WHERE id = ?"
    cursor.execute(statement, [estadio, partido, precio, sector, id])
    db.commit()
    return True

#esta funcion no la pide, pero sirve para borrar una copa
def delete_copa(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM copa WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

#sirve para obtener una copa en específico de acuerdo a un id
def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, estadio, partido, precio, sector FROM copa WHERE id = ?"
    cursor.execute(statement, [id])
    single_copa = cursor.fetchone()
    id = single_copa[0]
    estadio = single_copa[1]
    partido = single_copa[2]
    precio = single_copa[3]
    sector = single_copa[4]
    copa = Copa(id,estadio, partido, precio, sector)
    return copa.serialize()

#sirve para hacer una lisa de todas las copas disponibles
def get_copas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, estadio, partido, precio, sector FROM copa"
    cursor.execute(query)
    copa_list = cursor.fetchall()
    list_of_copas=[]
    for copa in copa_list:
        id = copa[0]
        estadio = copa[1]
        partido = copa[2]
        precio = copa[3]
        sector = copa[4]
        copa_to_add = copa(id,estadio, partido, precio, sector)
        list_of_copas.append(copa_to_add)
    return list_of_copas
