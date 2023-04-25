from __future__ import annotations
from bson import ObjectId
from typing import TypeVar

import mongoengine as me


class Document(me.Document):
    meta = {"abstract": True}

    @classmethod
    def get_doc(cls, _id: str | ObjectId):
        return cls.find_doc(id=_id)

    @classmethod
    def find_doc(cls: type[DocT], **kwargs) -> DocT | None:
        return cls.objects(**kwargs).first()

    @classmethod
    def find_docs(cls: type[DocT], **kwargs) -> list[DocT]:
        return list(cls.objects(**kwargs))

    @property
    def str_id(self) -> str:
        return str(self.pk)


DocT = TypeVar("DocT", bound=Document)
