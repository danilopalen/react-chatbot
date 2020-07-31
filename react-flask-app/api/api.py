from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# =======================================================DB MODELS===========================================================
class Details(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(40), unique = True, nullable = False)

class CarInfo(db.Model):
    rego = db.Column(db.String(10), primary_key = True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.Integer)
    
db.create_all()
# ======================================POST FUNCTIONS TO SAVE DATA TO DATABASE=====================================
@app.route('/add_car', methods = ['POST'])
def add_car():
    car_data = request.get_json()
    
    new_car = CarInfo(rego = car_data['rego'], make = car_data['make'], model = car_data['model'], year = car_data['year'])

    db.session.add(new_car)
    db.session.commit()

    return 'Done', 201

@app.route('/add_details', methods = ['POST'])
def add_details():
    details_data = request.get_json()
    
    new_detail = Details(id = details_data['id'], fname = details_data['fname'], lname = details_data['lname'], email = details_data['email'])

    db.session.add(new_detail)
    db.session.commit()

    return 'Done', 201
#----------------------------------------------POST INPUT TO CHATBOT API------------------------------------------------------
@app.route('/input', methods = ['GET','POST'])
def input():
    import collections
    import json
    from ibm_watson import AssistantV2
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

    # my bot
    my_apikey = 'YOL8n5EcRf2D1b8YrkT6ATix7o5TdcwNso5wYtXY2wIi'
    my_aid = '9097fa59-e0fa-4bad-b0e6-195f76bae232'
    my_url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/5acee416-015c-42ea-9ba1-e8549214ef5c'

    authenticator = IAMAuthenticator(my_apikey)
    assistant = AssistantV2(
        version='2020-04-01',
        authenticator=authenticator
    )

    assistant.set_service_url(my_url)

    session = assistant.create_session(
        assistant_id = my_aid
    ).get_result()

    if request.method == 'POST':
        details_data = request.get_json()
        user_input = details_data['text']
    else:
        user_input = ''

    response = assistant.message(
        assistant_id = my_aid,
        session_id = session['session_id'], 
        input={
            'message_type': 'text',
            'text': user_input            
        }
    ).get_result()

    print(json.dumps(response, indent=2))

    return jsonify({
        'response' : response['output']['generic'][0]['text'],
        'output' : response
    })

# ===============================================GET DATA FROM DATABASE========================================================
@app.route('/details')
def details():
    customer_list = Details.query.all()    
    details = []

    for customer in customer_list:
        details.append({'id' : customer.id, 'firstname' : customer.fname, 'lastname' : customer.lname, 'email' : customer.email})
    
    return jsonify({
        'details' : details
    })

@app.route('/cars')
def cars():
    car_list = CarInfo.query.all()    
    cars = []

    for car in car_list:
        cars.append({'rego' : car.rego, 'make' : car.make, 'model' : car.model, 'year' : car.year})
    
    return jsonify({
        'cars' : cars
    })