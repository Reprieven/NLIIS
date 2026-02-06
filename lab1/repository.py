from database import SessionDep
from models.text import Text, Lemma
from sqlalchemy import select, join, delete
class TextRepository:
    
    @classmethod
    async def get_one(id: int, session: SessionDep):
        query = select(Text)
