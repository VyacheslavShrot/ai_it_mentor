from pydantic import BaseModel, constr


class Body(BaseModel):
    text: constr(min_length=5)
