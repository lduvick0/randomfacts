from fastapi import FastAPI
from pydantic import BaseModel
import random as rand

# Successfully able to launch backend server from main.py file (1 Point)
app = FastAPI()


# Users can successfully make a GET request to the specified endpoint (1 Point)
@app.get("/")
async def main():
    return{"test":"value"}
# The endpoint URL is /fact (1 Point)




# Each API call returns a random fact from your list of facts. (Each fact is an object with an "id" and a "fact".) (1 Point)
class Fact(BaseModel):
    id: int
    fact:str

fact_db = [Fact(id=1, fact="Human teeth are the only part of the body that cannot heal themselves."),
                 Fact(id=2, fact="It's illegal to own just one guinea pig in Switzerland."),
                 Fact(id=3, fact="'Mellifluous' is a sound that is pleasingly smooth and musical to hear."),
                 Fact(id=4, fact="The Spice Girls were originally a band called Touch.")]
@app.get("/fact/")
async def fact():
    if fact_db:
        randfact=rand.choice(fact_db)
        return randfact
    else:
        return {"error":"none"}
# "id" query parameter that allows the user to denote the specific fact they want returned by the index location of the fact (1 Points)
# Add another alternative endpoint–GET /fact/{id}--using a path parameter as a way to specify the index of the fact to return.
@app.get("/fact/{fact_id}")
async def fact(fact_id: int):
    for fact in fact_db:
        if fact.id==fact_id:
            return fact

    return None
# Extend your API with a new endpoint to allow users to add new facts (i.e. POST). The new fact should be appended to the list of facts. (2 Points)
@app.post("/add")
async def add_fact(fact: Fact):
    fact_db.append(fact)
    return fact

# Logical naming of variables and endpoints and code legibility (2 Points)

