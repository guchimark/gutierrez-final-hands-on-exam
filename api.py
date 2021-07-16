from flask import Flask, render_template
from flask_restful import request, abort, Api, Resource

app = Flask(__name__)

SERVICES = {
    1 : {"id" : 1, "name" : "FoodPanda", "url" : "https://www.foodpanda.com/", "category" : "Delivery Service", "description" : "foodpanda allows users to conveniently discover food around their neighbourhood and directly order their favourite meals online or via mobile.", "fb_url" : "https://www.facebook.com/foodpandaphilippines"},
    2 : {"id" : 2, "name" : "iRehistro", "url" : "https://irehistro.comelec.gov.ph/", "category" : "Government Service", "description" : "An online portal for voter's registration", "fb_url" : ""},
    3 : {"id" : 3, "name" : "PhilHealth E-Register", "url" : "https://eregister.philhealth.gov.ph/", "category" : "Government Service", "description" : "An online registration for PhilHealth clients.", "fb_url" : ""},
}

@app.route('/')
def index():
    return render_template('index.html', 
    data = SERVICES,
    )

@app.route('/manage')
def manage():
    return render_template('manage.html')

api = Api(app)

class ManageServices(Resource):
    def get(self):
        service_list = [service_data for id, service_data in SERVICES.items()]
        response_data = { "data" : service_list }
        return response_data

    def post(self):
        request_data = request.get_json(force=True)

        if not request_data \
            or not 'name' in request_data \
            or not 'url' in request_data \
            or not 'category' in request_data \
            or not 'description' in request_data \
            or not 'fb_url' in request_data:

            abort(400)

        new_service_id = int(max(SERVICES.keys())) + 1
        new_service = {
            "id" : new_service_id,
            "name" : request_data["name"],
            "url" : request_data["url"],
            "category" : request_data["category"],
            "description" : request_data["description"],
            "fb_url" : request_data["fb_url"]
        }
        
        SERVICES[new_service_id] = new_service

        return new_service, 201

    def put(self):
        request_data = request.get_json(force=True)

        update_service_id = int(request_data["id"])

        updated_service = {
            "id" : request_data["id"],
            "name" : request_data["name"],
            "url" : request_data["url"],
            "category" : request_data["category"],
            "description" : request_data["description"],
            "fb_url" : request_data["fb_url"]
        }

        SERVICES[update_service_id] = updated_service
        
        return updated_service, 200

    def delete(self):
        request_data = request.get_json(force=True)

        delete_service_id = int(request_data["id"])

        SERVICES.pop(delete_service_id)
        
        return '', 204

#class ManageServices2(Resource):

api.add_resource(ManageServices, '/api')
#api.add_resource(ManageServices2, '/api/' + row_id)

if __name__ == "__main__":
    app.run(debug = True)
