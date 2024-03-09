import datetime
import json
import os
import yaml
from pathlib import Path

from pydantic import BaseModel
from zipfile import ZipFile
from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


class UploadedFile(BaseModel):
    date_created: str
    date_modified: str
    file_name: str
    path: Path | None = None
    size: int
    uploader: str


STORAGE_ROOT = Path(r"/mnt/d/Documents/Test/storage")
CHUNK_SIZE = 1024 * 1024

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def upload_file(file: UploadFile):
    '''
    Receives Upload files
    '''
    print(f"{file.content_type=}")
    file_ext = file.filename.split(".").pop()
    print(f"{file_ext=}")
    if file_ext not in ["zip", "txt", "json"]:
        raise HTTPException(400, detail="Invalid document type")

    data = file.file
    return {"content": data, "file_name": file.filename}
 
@app.post("/upanddownload")
async def up_and_download_file(file: UploadFile):
    '''
    Returns YAML file
    '''
    print(f"{file.content_type=}")
    if file.content_type != "application/json":
        raise HTTPException(400, detail= "Invalid document type")
    else:
        date_str = datetime.datetime.today().strftime(r"%y%m%d")
        json_data = json.loads(file.file.read())

        old_file_name = file.filename
        filename = os.path.splitext(old_file_name)[0]
        new_filename = f"{filename}_{date_str}.yaml"
        
        saved_file_path = os.path.join(STORAGE_ROOT, new_filename)
        print(saved_file_path)
        with open(saved_file_path, "w") as x:
            yaml.dump(json_data, x)
        return FileResponse(path=saved_file_path, media_type="application/octet-stream", filename=new_filename)

@app.get("/contents")
async def list_directory():
    '''
    List directory in storage
    '''
    contents = os.listdir(STORAGE_ROOT)
    data = {}
    # for item in contents:
    #     data["id"]
    return {"files": contents }


# subapi = FastAPI()

# @subapi.get("/file")
# async def download(file_path: str):
#     '''
#     Downloads selected file
#     '''
#     print(f"download {file_path}")
#     # return FileResponse("files/")


# app.mount("/download", subapi)
# app.mount("/download", StaticFiles(directory=STORAGE_ROOT.joinpath("mount"), html=True))