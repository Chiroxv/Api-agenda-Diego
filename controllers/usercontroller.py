from db import conectar
from models import Usuario

def seleccionarUsuario(email,password):
    id = 0
    try:
        session = conectar()
        usuarios = session.query(Usuario).filter(Usuario.email == email, Usuario.password == password).all()
        if len(usuarios) > 0:
            id = usuarios[0].id
    except Exception as e:
        print(e)
    finally:
        session.close()
    return id