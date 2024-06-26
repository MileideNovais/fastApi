from fastapi import APIRouter
from WORKOUT_API.atleta.controller import router as atleta

api_router = APIRouter ()
api_router.include_router(atleta, prefix='atleta',  tags='atletas/' )