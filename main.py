from contextlib import asynccontextmanager
import httpx
from fastapi import FastAPI, HTTPException
import pandas as pd

#Dictionary where measurements will be stored
measurementsData = {} 

#API Url
measurementsUrl = 'http://localhost:3000/measurements' 

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Get measurements once at the start of the application from API and store them in a dictionary.
    Clear the dictionary when the application stops
    """
    response = httpx.get(measurementsUrl)
    if response.status_code != httpx.codes.OK:
        raise HTTPException(status_code=500, detail="Could not reach measurements API")
    measurementsData["measurements"] = response.json()
    yield
    measurementsData.clear()

app = FastAPI(lifespan=lifespan)

def getCleanData():
    """
    Get cleaned pandas dataframe with correct number format
    """
    
    #Create pandas dataframes from the two dictionaries gotten from the API
    cols = ['precip', 'temp', 'hum']
    df = pd.DataFrame.from_dict(measurementsData["measurements"][0], orient='index', columns=cols)
    dfbis = pd.DataFrame.from_dict(measurementsData["measurements"][1], orient='index', columns=cols)
    
    #Compare them and remove rows that do not match
    dfcompare = df.compare(dfbis)
    df = df.drop(index=dfcompare.index.values.tolist())
    dfbis = dfbis.drop(index=dfcompare.index.values.tolist())
    
    #Remove rows that have empty values
    df = df.dropna()
    
    df = df.astype(float)
    return df

@app.get("/api/data")
async def data():
    """
    Get full cleaned dataset 
    """
    df = getCleanData()
    return df.to_dict('index')

@app.get("/api/summary")
async def summary():
    """
    Gets quick overview of the dataset. Returns a dictionary containing statistics about the measurements
    """
    df = getCleanData()
    #Use describe function to get stats and remove unnecessary
    summary = df.describe().drop(index=['count','std', '25%', '50%', '75%'])
    return {"totalMeasurementsCount" : df.shape[0], "columns" : summary.to_dict()}

