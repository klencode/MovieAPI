from fastapi import FastAPI, HTTPException
from omdb_client import OMDbClient
from models import MovieDetails
from dotenv import load_dotenv
from utils import handle_api_error
import os

app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Create IMDb client instance
api_key = os.getenv("OMDB_API_KEY")
omdb_client = OMDbClient(api_key)

@app.get("/")
async def root():
    return {"message": "Welcome to the OMDb FastAPI Interface"}

@app.get("/search/{query}")
async def search_movie(query: str):
    """Search for a movie by title."""
    result = omdb_client.search_movie(query)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=f"No results found for '{query}'")
    return result

@app.get("/movie/{movie_id}", response_model=MovieDetails)
async def get_movie_details(movie_id: str):
    """Retrieve movie details using OMDb ID."""
    result = omdb_client.get_movie_details(movie_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=f"Movie not found for ID '{movie_id}'")
    return result

@app.get("/movie/title/{title}", response_model=MovieDetails)
async def get_movie_by_title(title: str):
    """Retrieve movie details by title."""
    result = omdb_client.get_movie_by_title(title)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=f"Movie not found for title '{title}'")
    return result


# print(f"OMDB API Key: {api_key}")