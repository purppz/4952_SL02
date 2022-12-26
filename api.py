from fastapi import FastAPI, Request, Response

app = FastAPI()

users = [
{
"id": 1,
"name": "Hello World"
}
]

@app.post("/valdorio/")
async def post_valdorio(request: Request, response: Response):
    users.append(await request.json())
    response.status_code = 200

@app.get("/valdorio/{id}")
async def get_valdorio(id: int, request: Request, response: Response):
    if isinstance(id, int): 
        for x in users: 
            if id == x["id"]:  
                return x
    else:
        response.status_code = 404

@app.get("*")
async def not_found(request: Request, response: Response):
    response.status_code = 404
    return "Not found"
