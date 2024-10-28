from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from random import randint
from sqlmodel import select
from movie import MovieModel
from schemas import MovieSchema


app = FastAPI()

create_db_and_tables()


@app.post("/movies")
async def create_movie(movie_date: MovieSchema, datebase: SessionDep):
    movie = MovieModel(nombre_pelicula=movie_date.nombre_pelicula, ano_estreno=movie_date.ano_estreno, duracion=movie_date.duracion, director=movie_date.director, clasificacion=movie_date.clasificacion, genero=movie_date.genero)
    datebase.add(movie)
    datebase.commit()
    datebase.refresh(movie)
    return movie
    
    
@app.get("/movies")
async def get_users(database: SessionDep):
    statement = select(MovieModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_user_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MovieModel, movie_id)
    
    if not movie: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie no encontrado")
    return movie
    