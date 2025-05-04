from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")  # Make sure this file exists in the same directory

@app.route("/")
def home():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        inputs = [
            float(request.form["smoking_rate"]),
            float(request.form["pharma_presc"]),          # FIXED name
            float(request.form["price_index"]),
            float(request.form["afford_index"]),          # FIXED name
        ]
        prediction = model.predict([inputs])[0]
        prediction = round(prediction, 2)
    except Exception as e:
        prediction = f"Error: {e}"
    
    return render_template("index.html", prediction=prediction, form=request.form)

if __name__ == "__main__":
    app.run(debug=True)
