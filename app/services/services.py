from sqlalchemy.orm import Session
from app.database.database import Base
from app.models.models import Warehouse, Package, Waybill
import app.schemas.schemas as schemas
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def create_warehouse(db: Session, warehouse: schemas.WarehouseCreate):
    try:
        new_warehouse = Warehouse(
            warehouse_name = warehouse.warehouse_name,
            location = warehouse.location
        )
        db.add(new_warehouse)
        db.commit()
        db.refresh(new_warehouse)
        return new_warehouse
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Lỗi không xác định")
    
def get_warehouse(db: Session, warehouse_id: int):
    result = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="ID không tồn tại")
    return result