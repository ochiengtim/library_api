from sqlalchemy.orm import Session
from app import models, schemas

def create_category(db: Session, category: schemas.CategoryBase):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def update_category(db: Session, category_id: int, new_data: schemas.CategoryBase):
    category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if not category:
        return None
    category.name = new_data.name
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category
