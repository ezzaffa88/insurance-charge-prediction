from flask import Flask,request,jsonify
from sklearn import linear_model
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
@app.route('/predict', methods=['GET'])
def get_prediction():
 age = int(request.args.get('age'))
 bmi = float(request.args.get('bmi'))
 children = int(request.args.get('children'))
 smoke = int(request.args.get('smoker'))
 male = int(request.args.get('male'))
 modelname = 'Insurance_charge_prediction.pkl'
 #print('Loading %s' % modelname)
 
 loaded_model = pickle.load(open(modelname, 'rb'), encoding='latin1')
 insurance_charges = loaded_model.predict([[age, bmi,children,smoke,male]])
 #print('----------response-----------',insurance_charges)
 return jsonify(charges=insurance_charges[0])
  
if __name__ == '__main__':
 app.run(port=5000,host='0.0.0.0')
 #app.run(debug=True)