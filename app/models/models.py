from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    warehouse_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    packages = relationship("Package", back_populates="warehouse")


class Package(Base):
    __tablename__ = "packages"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    package_code = Column(String(100), nullable=False, unique=True)
    weight = Column(Float, nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    warehouse = relationship("Warehouse", back_populates="packages")
    waybill = relationship("Waybill", back_populates="package", uselist=False)


class Waybill(Base):
    __tablename__ = "waybills"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tracking_number = Column(String(100), nullable=False, unique=True)
    shipping_status = Column(String(100), nullable=False)
    package_id = Column(Integer, ForeignKey("packages.id"), unique=True, nullable=False)
    package = relationship("Package", back_populates="waybill")