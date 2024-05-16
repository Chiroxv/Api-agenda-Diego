from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

base = declarative_base()

class Usuario(base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, email={self.email}, password={self.password})>"

class Contacto(base):
    __tablename__ = 'Contacto'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fechaCreacion = Column(DateTime, default=datetime.utcnow, name="fechaCreacion")

    def __repr__(self):
        return f"<Contacto(id={self.id}, nombre={self.nombre}, apellido={self.apellido}, direccion={self.direccion}, email={self.email}, telefono={self.telefono}, fecha_creacion={self.fecha_creacion})>"

class pertenece(base):
    __tablename__ = 'pertenece'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_contacto = Column(Integer, nullable=False)