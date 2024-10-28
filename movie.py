from sqlmodel import SQLModel, Field

class MovieModel(SQLModel, table=True):
    __tablename__="movies"
    
    id: int = Field(primary_key = True)
    nombre_pelicula: str
    ano_estreno: str
    duracion: str
    director: str
    clasificacion: str
    genero: str
    
    
    
    