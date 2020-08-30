from flask import Flask, Response, request, json
import pickle
import pandas as pd

app = Flask(__name__)

filename = "api/iris_model.pkl"
print(open(filename, "rb"))
model = pickle.load(open(filename, "rb"))

def is_data_correct(data):
  return len(data) == 4

def predict_data(data_dict):
  data = pd.DataFrame(data_dict, index=[0])
  prediction = model.predict_proba(data)
  return prediction.tolist()[0]

@app.route("/predict", methods=["POST"])
def predict():
  try:
    data = request.get_json()
    print(data)
    if is_data_correct(data):
      prediction = {}
      prediction["input"] = data 
      prediction["score"] = predict_data(data)
      response = app.response_class(
        response=json.dumps(prediction),
        status=200
      )
    return response
  except Exception as ex:
    return Response(status=400, response=ex)


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=3001)