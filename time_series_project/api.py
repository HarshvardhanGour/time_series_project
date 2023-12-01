from load_model import load_model_timeseries
dax_model,ftse_model,nikkei_model,spx_model=load_model_timeseries()
from flask import Flask,request,render_template,jsonify

app=Flask(__name__)

@app.route("/first_page",methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/predict_output",methods=["GET","POST"])
def prediction():
    date_value=request.form.get("date_input")
    model_name=request.form.get("mdel_name")
    if model_name=="spx":
        prediction=spx_model.predict(start=date_value,end=date_value)
        print(prediction)
        print(prediction[0])
        
        return jsonify({f"The prediction of the spx value for the date {date_value}": prediction[0]})
    elif model_name=="ftse":
        prediction=ftse_model.predict(start=date_value,end=date_value)[0]
        return jsonify({f"The prediction of the ftse value for the date {date_value}": prediction})
    elif model_name=="dax":
        prediction=dax_model.predict(start=date_value,end=date_value)[0]
        return jsonify({f"The prediction of the dax value for the date {date_value}": prediction})
    elif model_name=="nikkei":
        prediction=nikkei_model.predict(start=date_value,end=date_value)[0]
        return jsonify({f"The prediction of the nikkei value for the date {date_value}": prediction})
    else:
        return "The model selection is not same as spx or dax or ftse or nikkei."
if __name__=="__main__":
    app.run(host="127.0.0.1",port="8080",debug=True)