import pickle 
import numpy as np
import pandas as pd
import pickle
import json

def predict(df):
    
    df['PM25']=float(df['PM25'])
    df['PM10']=float(df['PM10'])
    df['NO']=float(df['NO'])
    df['NO2']=float(df['NO2'])
    df['NOx']=float(df['NOx'])
    df['NH3']=float(df['NH3'])
    df['CO']=float(df['CO'])
    df['SO2']=float(df['SO2'])
    df['O3']=float(df['O3'])
    df['Benzene']=float(df['Benzene'])
    df['Toluene']=float(df['Toluene'])
    df['Xylene']=float(df['Xylene'])
    
    
    city_map={
        "Ahmedabad":12,
        "Aizawl":13,
        "Amaravati":14,
        "Amritsar":15,
        "Bengaluru":16,
        "Bhopal":17,
        "Brajrajnagar":18,
        "Chandigarh":19,
        "Chennai":20,
        "Coimbatore":21,
        "Delhi":22,
        "Ernakulam":23,
        "Gurugram":24,
        "Guwahati":25,
        "Hyderabad":26,
        "Jaipur":27,
        "Jorapokhar":28,
        "Kochi":29,
        "Kolkata":30,
        "Lucknow":31,
        "Mumbai":32,
        "Patna":33,
        "Shillong":34,
        "Talcher":35,
        "Thiruvananthapuram":36,
        "Visakhapatnam":37
    }

    city_index = city_map[df['city'].iloc[0]]
    
    x = np.zeros(38)
    x[0] = df['PM25'].iloc[0]
    x[1] = df['PM10'].iloc[0]
    x[2] = df['NO'].iloc[0]
    x[3] = df['NO2'].iloc[0]
    x[4] = df['NOx'].iloc[0]
    x[5] = df['NH3'].iloc[0]
    x[6] = df['CO'].iloc[0]
    x[7] = df['SO2'].iloc[0]
    x[8] = df['O3'].iloc[0]
    x[9] = df['Benzene'].iloc[0]
    x[10] = df['Toluene'].iloc[0]
    x[11] = df['Xylene'].iloc[0]

    x[city_index] = 1
    
    model = pickle.load(open("aqi_daily_model.pickle", 'rb'))
    aqi=model.predict([x])[0]
    print("Aqi value is this",aqi)
    
    if aqi <= 50:
        return 'GOOD'
    elif aqi <= 100:
        return 'SATISFACTORY'
    elif aqi <= 200:
        return 'MODERATE'
    elif aqi <= 300:
        return 'POOR'
    elif aqi <= 400:
        return 'VERY POOR'
    else:
        return 'SEVERE'