from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Test 1 2 3"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)