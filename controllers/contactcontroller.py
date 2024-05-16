from db import conectar
from models import Contacto, pertenece
from sqlalchemy import or_

def seleccionar_contactos(id_usuario, campo, orden):
    contactos = None  # Inicializar contactos
    session = conectar()

    try:
        if campo == "ID" and orden == "ASC":
            contactos = session.query(Contacto).join(pertenece, Contacto.id == pertenece.id_contacto).filter(pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
        elif campo == "ID" and orden == "DESC":
            contactos = session.query(Contacto).join(pertenece, Contacto.id == pertenece.id_contacto).filter(pertenece.id_usuario == id_usuario).order_by(Contacto.id.desc()).all()
        elif campo == "NOMBRE" and orden == "ASC":
            contactos = session.query(Contacto).join(pertenece, Contacto.id == pertenece.id_contacto).filter(pertenece.id_usuario == id_usuario).order_by(Contacto.nombre).all()
        elif campo == "NOMBRE" and orden == "DESC":
            contactos = session.query(Contacto).join(pertenece, Contacto.id == pertenece.id_contacto).filter(pertenece.id_usuario == id_usuario).order_by(Contacto.nombre.desc()).all()

        print("Contactos encontrados:", contactos)  # Agregar mensaje de depuración

    except Exception as e:
        print("Error al seleccionar contactos:", e)  # Agregar mensaje de depuración
        contactos = []  # Manejar el caso de error estableciendo contactos como una lista vacía

    finally:
        if session:
            session.close()  # Cerrar la sesión solo si se creó correctamente

    return contactos

def seleccionar_contacto(id):
    try:
        session = conectar()
        contacto = session.query(Contacto).filter(Contacto.id == id).all()[0]
    except Exception as e:
        print(e)

    finally:
            session.close()

    return contacto

def busqueda_contactos(id_usuario, value):
    contactos = []  # Inicializar contactos fuera del bloque try
    try:
        session = conectar()
        contactos = session.query(Contacto).join(pertenece, Contacto.id == pertenece.id_contacto).filter(pertenece.id_usuario == id_usuario).filter(or_(Contacto.nombre.ilike('%'+value+'%'), Contacto.apellido.ilike('%'+value+'%'), Contacto.direccion.ilike('%'+value+'%'), Contacto.email.ilike('%'+value+'%'))).order_by(Contacto.nombre).all()
        contactos_dict = []
        for contacto in contactos:
            contacto_dict = {
                'id': contacto.id,
                'apellido': contacto.apellido,
                'direccion': contacto.direccion,
                'nombre': contacto.nombre,
                'email': contacto.email,
                'telefono': contacto.telefono,
                'fechaCreacion': str(contacto.fechaCreacion)
            }
            contactos_dict.append(contacto_dict)

        return contactos_dict
    except Exception as e:
        print(e)
    finally:
        session.close()


def insertar_contacto(id_usuario, nombre, apellido, direccion, email, telefono):
    try:
        contacto = Contacto(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            email=email,
            telefono=telefono
        )
        session = conectar()
        session.add(contacto)
        session.commit()

        session.refresh(contacto)
        id_contacto = contacto.id

        relacion = pertenece(
            id_usuario=id_usuario,
            id_contacto=id_contacto
        )
        session.add(relacion)
        session.commit()

        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if session:
            session.close()

def actualizar_contacto(id, nombre, apellido, direccion, email, telefono):
    try:
        session = conectar()
        contacto = session.query(Contacto).get(id)
        contacto.nombre = nombre
        contacto.apellido = apellido
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono
    
        session.add(contacto)
        session.commit()

        return True
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()

def eliminar_contacto(id_usuario, id_contacto):
    try:
        session = conectar()
        session.query(pertenece).filter(pertenece.id_contacto == id_contacto).filter(pertenece.id_usuario == id_usuario).delete()
        contactO = session.query(Contacto).get(id_contacto)
        session.delete(contactO)
        session.commit()

        return True
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()