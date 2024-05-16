from flask import Flask, jsonify, request, session
from flask import Blueprint
import controllers.usercontroller as usercontroller


user_api = Blueprint('user_api',__name__)


@user_api.route("/usuario",methods = ['GET'])
def getUsuario():
    parametros = request.args
    email = parametros['email']
    password = parametros['password']
    result = usercontroller.seleccionarUsuario(email,password)
    return jsonify({'result':result})