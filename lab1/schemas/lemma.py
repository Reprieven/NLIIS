from pydantic import BaseModel, Field


class SLemmaBase(BaseModel):
    lemma: str
    morph: str
    role: str


class SLemmaAdd(SLemmaBase):
    text_id: int = Field(..., ge=1)
    word: str


class SLemmaUpdate(SLemmaBase):
    pass


class SLemmaResponse(SLemmaBase):
    id: int
    word: str
