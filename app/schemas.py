from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryOut(CategoryBase):
    category_id: int

    class Config:
        from_attributes = True
