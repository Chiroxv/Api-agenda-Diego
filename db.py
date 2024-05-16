from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:xNevir27@localhost:5432/Agenda'

def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print("Conexion a base de datos LISTA")
    else:
        print("Conexion invalida")
    return s