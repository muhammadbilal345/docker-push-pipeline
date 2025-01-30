from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def index():
    return "homepage"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)