from flask import Blueprint
from app.dessal_db.controller import DessalController
dessal_db_api = Blueprint('dessal_db_api',__name__)

#rotas de conexão ao database do dash-leaflet
#dessal_db_api.add_url_rule(
#        '/', view_func = DessalController.as_view('aluno_create'), methods = ['GET'])