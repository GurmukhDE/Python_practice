from fastapi import FastAPI

app = FastAPI()

@app.get("/getUsers")

def get_user():
    return {"user1" : "Gurmukh"}


@app.post("/postUserDatatoTable")
def create_user(name, age, salary):
    return {"message": "User added successfully"}



