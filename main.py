from fastapi import FastAPI
import routes.affirmations_router as ar
import uvicorn

app = FastAPI(    
    title='Positive Affirmations API',
    version='0.0.1',
    description='Personal project with FastAPI')

app.include_router(ar.router, tags=['positive'])

if __name__ == '__main__':
  
    uvicorn.run("main:app", host="0.0.0.0", port=8003)



