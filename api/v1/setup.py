from fastapi import APIRouter

router = APIRouter(prefix="/setup", tags=["setup"])


@router.get("/")
async def api_setup():
    return {"detail": "Api is setup and ready to go!"}
