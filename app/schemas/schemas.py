from pydantic import Field, BaseModel, ConfigDict
from typing import Optional


class WarehouseCreate(BaseModel):
    warehouse_name: str = Field(..., min_length=5)
    location: str = Field(..., min_length=5)


class PackageResponse(BaseModel):
    id: int
    package_code: str
    weight: float
    model_config = ConfigDict(from_attributes=True)


class WarehouseDetailResponse(BaseModel):
    id: int
    warehouse_name: str
    location: str
    packages: list[PackageResponse]
    model_config = ConfigDict(from_attributes=True)


class PackageUpdate(BaseModel):
    package_code: Optional[str] = Field(None)
    weight: Optional[float] = Field(None)


class WaybillResponse(BaseModel):
    tracking_number: str
    shipping_status: str
    model_config = ConfigDict(from_attributes=True)