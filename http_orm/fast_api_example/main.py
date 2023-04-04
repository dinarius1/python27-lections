from fastapi import FastAPI

app = FastAPI()

@app.get('/')   
def hello():
    return {'message' : 'hello world'}   #пишем все в словари, так как наш декоратор затем преоьразует наш код в формат json

@app.post('/create')
def create():
    return {'message' : 'created'}


@app.delete('/delete')
def delete():
    return {'message' : 'deleted'}