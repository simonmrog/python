from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  BMI = 0
  if request.method == "POST" and "weight-input" in request.form and "height-input" in request.form:
    weight = float(request.form.get("weight-input"))
    height = float(request.form.get("height-input"))
    BMI = round(weight / (height / 100) ** 2, 1)

  return render_template("index.html", BMI=BMI)

if __name__ == "__main__":
  app.run(host="0.0.0.0")