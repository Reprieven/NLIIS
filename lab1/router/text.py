from database import SessionDep
from schemas.lemma import SLemmaAdd, SLemmaUpdate, SLemmaResponse
from schemas.text import STextAdd, STextUpdate, STextResponse
from fastapi import APIRouter, status, HTTPException
from repository import LemmaRepository, TextRepository

router = APIRouter(prefix="/text", tags=["Тексты"])


@router.get("/{id}", responce_model=STextResponse, status_code=status.HTTP_200_OK)
async def get_text(id: int, session: SessionDep):
    text = await TextRepository.get_one(id, session)
    if text is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Text with id {id} not found"
        )
    return text
