from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def getData():
    return "welcome to home"