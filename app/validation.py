from pydantic import BaseModel


class PhraseJSON(BaseModel):
    """Validate getting of json from the phrase"""
    phrase: str
