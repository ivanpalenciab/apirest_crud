from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String
from cofig.db import meta,engine

#se indica las tablas y los tipos de datos, meta es lo que indica cual es la base de datos
users = Table("users",meta,Column(
    "id",Integer,primary_key=True),
    Column("name",String(255)),
    Column("email",String(255))
    )

#se crea la tabla en engine
meta.create_all(engine)