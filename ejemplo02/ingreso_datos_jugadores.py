from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

jugadores = open("data/datos_jugadores.txt","r")

registros = jugadores.readlines()
for j in registros:
    cl = j.split(";")[0]
    pos = j.split(";")[1]
    dor = j.split(";")[2]
    nom = j.split(";")[3]

    jugador = Jugador(club_id=cl,posicion=pos,dorsal=dor,nombre=nom)
    session.add(jugador)
    #session.query(Club).filter_by(nombre="LDU").one()


session.commit()

