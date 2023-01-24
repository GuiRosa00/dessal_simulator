from flask import request,jsonify,render_template
from flask.views import MethodView

from app.extensions import db


class DessalController(MethodView): #/
    def get(self):
        """get(self)->dict,int
        mostra todos os bancos de dessalinização registrado no dash-leaflet"""
        #
        #
        #
        #return jsonify([aluno.json() for aluno in aluno]),200
        pass

