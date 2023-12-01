import joblib

def load_model_timeseries():
    dax_model=joblib.load(r"C:\Users\ADITI GUPTA\Desktop\time_series_project\dax_model.pkl")
    ftse_model=joblib.load(r"C:\Users\ADITI GUPTA\Desktop\time_series_project\ftse_model.pkl")
    nikkei_model=joblib.load(r"C:\Users\ADITI GUPTA\Desktop\time_series_project\nikkei_model.pkl")
    spx_model=joblib.load(r"C:\Users\ADITI GUPTA\Desktop\time_series_project\spx_model.pkl")
    return dax_model,ftse_model,nikkei_model,spx_model
