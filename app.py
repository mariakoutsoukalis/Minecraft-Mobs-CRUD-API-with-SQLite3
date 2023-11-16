from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import actions

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# GET Request to Access Home of API.
@app.route("/", methods=["GET"])
def api_home():
    return jsonify({"message": "Welcome to the Minecraft Mobs API!"})

# GET Request to Access API Entry Point.
@app.route("/api", methods=["GET"])
def api_access():
    return jsonify({"message": "This API supports access to GET, POST, PATCH, and DELETE requests."})

# GET Request to Access All Mob Data.
@app.route("/api/mobs", methods=["GET"])
def api_get_mobs():
    return jsonify(actions.get_mobs())

# GET Request to Access Single Mob Data by ID.
@app.route("/api/mobs/<int:mob_id>", methods=["GET"])
def api_get_mob_by_id(mob_id):
    return jsonify(actions.get_mob_by_id(mob_id))

# POST Request to Add New Mob to Database.
@app.route("/api/mobs", methods=["POST"])
def api_add_mob():
    new_mob = request.json
    return jsonify(actions.create_mob(new_mob))

# PATCH Request to Update One Mob Metric for Single Mob in Database.
@app.route("/api/mobs/<int:mob_id>", methods=["PATCH"])
def api_update_mob(mob_id):
    new_mob_info = request.json
    return jsonify(actions.update_mob(mob_id, new_mob_info))

# DELETE Request to Delete Mob from Database.
@app.route("/api/mobs/<int:mob_id>", methods=["DELETE"])
def api_delete_mob(mob_id):
    return jsonify(actions.delete_mob(mob_id))

# Error-Handling Routing Function for 404 Resource Not Found.
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Page Not Found!"}), 404)


if __name__ == "__main__":
    app.run(debug=True)