from flask import Flask, jsonify, request
from flask import Blueprint

import controllers.contactcontroller as contactController


contact_api = Blueprint('contact_api',__name__)


@contact_api.route('/contactos', methods=['GET'])
def getContactos():
    parametros = request.args
    id_usuario = parametros.get('id_usuario')
    campo = parametros.get('campo')
    orden = parametros.get('orden')

    if not all([id_usuario, campo, orden]):
        return jsonify({'error': 'Faltan parámetros en la solicitud'}), 400

    contactos = contactController.seleccionar_contactos(id_usuario, campo, orden)

    # Convertir objetos Contacto a diccionarios
    contactos_dict = []
    for contacto in contactos:
        contacto_dict = {
            'id': contacto.id,
            'apellido': contacto.apellido,
            'direccion': contacto.direccion,
            'nombre': contacto.nombre,
            'email': contacto.email,
            'telefono': contacto.telefono,
            'fechaCreacion': str(contacto.fechaCreacion)  # Convertir fecha a cadena
        }
        contactos_dict.append(contacto_dict)

    return jsonify(contactos_dict)


@contact_api.route('/contacto', methods=['GET'])
def getContacto():
    parametros = request.args
    id_contacto = parametros.get('id_contacto')

    if not id_contacto:
        return jsonify({'error': 'Falta el parámetro id_contacto en la solicitud'}), 400

    contacto = contactController.seleccionar_contacto(id_contacto)

    if not contacto:
        return jsonify({'error': 'Contacto no encontrado'}), 404

    contacto_dict = {
        'id': contacto.id,
        'apellido': contacto.apellido,
        'direccion': contacto.direccion,
        'nombre': contacto.nombre,
        'email': contacto.email,
        'telefono': contacto.telefono,
        'fechaCreacion': str(contacto.fechaCreacion)
    }

    return jsonify(contacto_dict)

@contact_api.route('/contactStr', methods = ['GET'])
def getContactoStr():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    value = parametros['value']
    contactos = contactController.busqueda_contactos(id_usuario,value)

    return jsonify(contactos)

@contact_api.route('/contacto', methods=['POST'])
def insertContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    nombre = parametros['nombre']
    apellido = parametros['apellido']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros ['telefono']

    result = contactController.insertar_contacto(id_usuario, nombre, apellido, direccion, email, telefono)

    return jsonify({'result':result})

@contact_api.route('/contacto', methods=['PUT'])
def updateContacto():
    parametros = request.args
    id = parametros['id']
    nombre = parametros['nombre']
    apellido = parametros['apellido']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']

    result = contactController.actualizar_contacto(id,nombre,apellido,direccion,email,telefono)
    
    return jsonify({'result':result})

@contact_api.route('/contacto', methods=['DELETE'])
def deleteContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    id_contacto = parametros['id_contacto']
    result = contactController.eliminar_contacto(id_usuario, id_contacto)

    return jsonify({'result':result})