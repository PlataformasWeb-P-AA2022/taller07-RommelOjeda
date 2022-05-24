from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

club = open("data/datos_clubs.txt","r")
registroc = club.readlines()
for c in registroc:
    nom = c.split(";")[0]
    dep = c.split(";")[1]
    fun = c.split(";")[2]
    equipo = Club(nombre=nom,deporte=dep,fundacion=fun)
    session.add(equipo)

session.commit()

