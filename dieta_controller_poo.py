from dieta_db import get_db
from class_dieta import Dieta

#hago la funcion para insertar dietas faltantes
def insert_dieta(id, restriction, restriccion, USD):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO dieta (id, restriction, restriccion, USD) \
    VALUES ( ?, ?, ?, ? )"
    cursor.execute(statement, [id, restriction, restriccion, USD])
    db.commit()
    return True

#esta funcion no la pide, pero puede llegar a ser util, si se desean actualizar los precios de las dietas
def update_dieta(id, restriction, restriccion, USD):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE dieta SET id = ?, restriction = ?, restriccion= ?, USD= ? \
    WHERE id = ?"
    cursor.execute(statement, [restriction, restriccion, USD, id])
    db.commit()
    return True

#esta funcion no la pide, pero sirve para borrar una dieta
def delete_dieta(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM dieta WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

#sirve para obtener una dieta en específico de acuerdo a un id
def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, restriction, restriccion, USD FROM dieta WHERE id = ?"
    cursor.execute(statement, [id])
    single_dieta = cursor.fetchone()
    id = single_dieta[0]
    restriction = single_dieta[1]
    restriccion = single_dieta[2]
    USD = single_dieta[3]
    dieta = Dieta(id,restriction, restriccion, USD)
    return dieta.serialize()

#sirve para hacer una lisa de todas las dietas disponibles
def get_dietas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, restriction, restriccion, USD FROM dieta"
    cursor.execute(query)
    dieta_list = cursor.fetchall()
    list_of_dietas=[]
    for dieta in dieta_list:
        id = dieta[0]
        restriction = dieta[1]
        restriccion = dieta[2]
        USD = dieta[3]
        dieta_to_add = Dieta(id,restriction, restriccion, USD)
        list_of_dietas.append(dieta_to_add)
    return list_of_dietas
