from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime

class Text(Base):
    __tablename__ = 'texts'
    id: Mapped[int] = mapped_column(init=False, primary_key = True)
    name: Mapped[str]
    text: Mapped[str]
    date: Mapped[DateTime] = mapped_column(default = datetime.now())


class Lemma(Base):
    __tablename__ = 'lemmas'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    text_id: Mapped[str] = mapped_column(ForeignKey('texts.id', ondelete="CASCADE"))
    word: Mapped[str]
    lemma: Mapped[str]
    morph: Mapped[str]
    role: Mapped[str]



