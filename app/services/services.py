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


def update_package(db: Session, package_id: int, package_data: schemas.PackageUpdate):
    db_package = db.query(Package).filter(Package.id == package_id).first()
    if db_package is None:
        raise HTTPException(
            status_code=404, detail="Không tìm thấy kiện hàng với ID này")

    update_data = package_data.model_dump(exclude_unset=True)

    try:
        for key, value in update_data.items():
            setattr(db_package, key, value)
        db.commit()
        db.refresh(db_package)
        return db_package
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Lỗi không xác định khi cập nhật dữ liệu")


def delete_waybill(db: Session, waybill_id: int):
    db_waybill = db.query(Waybill).filter(Waybill.id == waybill_id).first()

    if db_waybill is None:
        raise HTTPException(
            status_code=404, detail="Không tìm thấy vận đơn để xóa")

    try:
        db.delete(db_waybill)
        db.commit()
        return {"message": f"Xóa thành công vận đơn có ID {waybill_id}"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Lỗi hệ thống không thể xóa vận đơn")
