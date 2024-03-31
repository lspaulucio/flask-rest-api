from mongoengine import Document
from flask_restx import Namespace, Resource

api = Namespace("Health", description="Application Health")


@api.route("/")
class HealthCheck(Resource):
    @api.response(200, "Success")
    def get(self):
        db = Document._get_db()
        status = db.command("serverStatus")["ok"]
        if status == 1:
            return {"message": "Healthy!"}, 200
