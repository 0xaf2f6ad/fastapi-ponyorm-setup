from fastapi import APIRouter
from . import auth, media, debug, users, m_upload, categories, announcement


router = APIRouter()

router.include_router(auth.router)
router.include_router(media.router)
router.include_router(m_upload.router)
router.include_router(debug.router)
router.include_router(users.router)
router.include_router(categories.router)
router.include_router(announcement.router)
