from typing import Dict
from pydantic import BaseModel

class ProductoInDB(BaseModel):
  codigo_producto:str
  nombre:str
  cantidad_disponible:int
  costo_adquisicion:int
  precio_venta:int
  fecha_caducidad:str

basedatos_producto=Dict[str,ProductoInDB]

basedatos_producto={
  "ARRZ":ProductoInDB(**{"codigo_producto":"ARRZ",
                          "nombre":"Arroz",
                          "cantidad_disponible":200,
                          "costo_adquisicion":800,
                          "precio_venta":1000,
                          "fecha_caducidad":"25-02-2022"




  })

}


def get_producto(codigo:str):
  if codigo in basedatos_producto.keys():
    return basedatos_producto[codigo]
  else:
    return None


def actualizar_producto(producto_in_db: ProductoInDB):
  basedatos_producto[producto_in_db.codigo_producto]=producto_in_db
  return producto_in_db



