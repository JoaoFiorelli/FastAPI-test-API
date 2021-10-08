from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {'data': {'name': 'Fiorelli'}}

@app.get('/about')
def about():
    return {'data': {'INFO': 'This API was created using the FastAPI framework, as a way of studying!'}}