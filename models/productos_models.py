from pydantic import BaseModel

class ProductoIn(BaseModel):
  codigo_producto : str
  nombre:str
  cantidad_disponible:int
  costo_adquisicion:int
  precio_venta:int
  fecha_caducidad:str
  


class ProductoOut(BaseModel):
  codigo_producto:str
  nombre:str
  cantidad_disponible:int
  costo_adquisicion:int
  precio_venta:int
  fecha_caducidad:str