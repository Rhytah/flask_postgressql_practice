from flask import Flask, jsonify,request,json,Blueprint, current_app as app
from api.controllers.incidents_controllers import IncidentsController
from flask_jwt_extended import JWTManager,jwt_required,create_access_token, get_jwt_identity

incident = Blueprint("incident",__name__)


incidents_controller=IncidentsController()
@incident.route('/api/v1/red-flags',methods=['GET'])
def fetch_red_flags():
    return incidents_controller.fetch_all_redflags()

@incident.route('/api/v1/red-flags/<int:redflag_id>', methods = ['GET'])
def fetch_single_red_flag(redflag_id):
    return incidents_controller.fetch_specific_redflag(redflag_id)

@incident.route('/api/v1/red-flags',methods=['POST'])
# @jwt_required
def add_red_flag():
    request_data=request.get_json()
    return incidents_controller.add_redflag(request_data)

@incident.route('/api/v1/red-flags/<int:redflag_id>',methods=['DELETE'])
def delete_redflag(redflag_id):
    return incidents_controller.delete_redflag(redflag_id)

@incident.route('/api/v1/red-flags/<int:redflag_id>/location', methods =['PATCH'])
def edit_location(redflag_id):
    return incidents_controller.edit_location(redflag_id)

@incident.route('/api/v1/red-flags/<int:redflag_id>/comment', methods =['PATCH'])
def edit_comment(redflag_id):
    return incidents_controller.edit_comment(redflag_id)