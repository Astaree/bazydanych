from flask_restful import Resource, reqparse
from flask import render_template, make_response

class Index(Resource):
    def get(self):  
        rendered_template = render_template('index.html',)
        response = make_response(rendered_template)
        response.headers['Content-Type'] = 'text/html' 
        return response