
from flask import Blueprint, request, jsonify
from resources.csv_manager import CSVManager

user = Blueprint('user', __name__)

@user.route('/user/getall', methods=["GET"])
def get_unique(**kwargs):
    try:
        unique = CSVManager().get_unique_persons()
        print(unique)
        return {'unique':unique}, 200
        
    except Exception as e:
        print(e)
        return {"status": "Server Error"}, 500
    
@user.route('/user/getperson', methods=["POST"])
def get_person(**kwargs):
    try:
        data = request.json.get('id')
        lis = CSVManager().get_all_person(data)
        print(lis)
        return {'lis':lis}, 200
        
    except Exception as e:
        print(e)
        return {"status": "Server Error"}, 500

