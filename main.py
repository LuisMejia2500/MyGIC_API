from db.producto_db import ProductoInDB
from db.producto_db import get_producto, actualizar_producto

from models.productos_models import ProductoIn, ProductoOut

from fastapi import FastAPI
from fastapi import HTTPException

api=FastAPI()

@api.post("/producto/")
async def auth_producto(producto_in:ProductoIn):
  producto_in_db =get_producto(producto_in.codigo_producto)
  if producto_in_db!= None:
    return{"estado":"El producto ya esta registrado"}
    #raise HTTPException(status_code=400,detail="El producto no existe")

  guardar_producto=actualizar_producto(ProductoInDB(**producto_in.dict()))
  return{"estado":"El producto fue registrado" + producto_in_db }
  
  
  
  

@api.get("/producto/informacion/{codigo_producto}")

async def get_producto_name(codigo_producto: str):
  producto_in_db=get_producto(codigo_producto)

  if producto_in_db == None:
    raise HTTPException(status_code=404,detail="El producto no existe")

  return ProductoOut(**producto_in_db.dict())
