from pydantic import BaseModel
from typing import List, Optional

# Response models to validate API data

class MovieSearchResult(BaseModel):
    id: str
    title: str
    year: str
    image: Optional[str]

class MovieDetails(BaseModel):
    id: str
    title: str
    year: str
    directors: Optional[str]
    cast: List[str]
    rating: Optional[str]
    genres: List[str]

class TopMoviesItem(BaseModel):
    id: str
    title: str
    year: str
    rating: Optional[str]

class TopMoviesResponse(BaseModel):
    items: List[TopMoviesItem]