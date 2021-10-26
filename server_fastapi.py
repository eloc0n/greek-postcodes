from fastapi import FastAPI
from scrape_wikipedia import extract_info

app = FastAPI()


@app.get("/greek-postcodes")
def extract_view():
    data = extract_info()
    return data
