from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File, Request
from fastapi.responses import JSONResponse, FileResponse

router = APIRouter(
    prefix="/files", 
    tags=["Files"])

from pathlib import Path

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB
uploads_folder = Path("uploads")
uploads_folder.mkdir(parents=True, exist_ok=True)

def is_allowed_file(filename):
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


@router.get("/")
async def get_uploaded_files():
    file_list = [str(file.name) for file in uploads_folder.iterdir() if file.is_file()]
    return JSONResponse(content={"files": file_list})


@router.get("/{filename}")
async def get_specific_file(filename: str, request: Request):
    print("client", request.client)

    file_path = uploads_folder / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
   

    file_url = f"{request.base_url}files/download_file/{file_path.name}"
   
    json_data = {
        "data": {
            "msg": "success",
            "file_url": file_url
        }
    }
    
    return JSONResponse(content=json_data)

@router.get("/download_file/{filename}")
async def download_file(filename: str):
    file_path = uploads_folder / filename
    return FileResponse(file_path)

@router.post("/upload")
async def upload_file(avatar: UploadFile = File(...)):
    print(avatar)
    if not is_allowed_file(avatar.filename):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # if avatar.content_length  > MAX_FILE_SIZE:
    #     raise HTTPException(status_code=400, detail="File size exceeds the limit")
    
    # Save the uploaded file to the "uploads" folder
    file_path = uploads_folder / avatar.filename
    with file_path.open("wb") as f:
        f.write(avatar.file.read())
    return {"msg": "success"}