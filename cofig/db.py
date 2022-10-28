from sqlalchemy import create_engine,MetaData

#se indica la ruta a la que se quiere conectar
engine = create_engine("mysql+pymysql://root:admin@localhost:3306/storedb")

meta = MetaData()

#se conceta la base de datos
con = engine.connect()