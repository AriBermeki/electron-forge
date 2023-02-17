from fastapi import FastAPI, HTTPException, Depends, status,File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import uvicorn





app = FastAPI()
origins =  [
    '*'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)




@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    data = df.to_dict(orient='records')
    return {"data": data}


if __name__ =="__main__":
    config = uvicorn.Config("run:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()