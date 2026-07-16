from fastapi import FastAPI, status, HTTPException, Depends
from app.database.database import Base, engine, get_db
import app.models.models as models
import app.schemas.schemas as schemas
import app.services.services as services
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/warehouses", response_model=schemas.WarehouseDetailResponse, status_code=status.HTTP_201_CREATED)
def create_warehouse(warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    return services.create_warehouse(db, warehouse)


@app.get("/warehouses/{warehouse_id}")
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return services.get_warehouse(db, warehouse_id)


@app.patch("/packages/{package_id}", response_model=schemas.PackageResponse, status_code=status.HTTP_200_OK)
def update_package(package_id: int, package: schemas.PackageUpdate, db: Session = Depends(get_db)):
    return services.update_package(db, package_id, package)


@app.delete("/waybills/{waybill_id}", status_code=status.HTTP_200_OK)
def delete_waybill(waybill_id: int, db: Session = Depends(get_db)):
    return services.delete_waybill(db, waybill_id)
