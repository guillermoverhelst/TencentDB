from fastapi import FastAPI
import model 
from config import engine
from router import router
app = FastAPI()
model.Base.metadata.create_all(bind=engine)
@app.get('/')
async def Home():
    return "Welcome home"

app.include_router(router, prefix="/book", tags=["book"])