import requests
from typing import Optional

class OMDbClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.omdbapi.com/"

    def _get(self, params: dict):
        """Generic GET request for OMDb API."""
        params['apikey'] = self.api_key  # Append API key to parameters
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    
    def search_movie(self, query: str):
        """Search for a movie by title."""
        params = {'s': query}
        return self._get(params)

    def get_movie_details(self, movie_id: str):
        """Retrieve details of a specific movie using its IMDb ID."""
        params = {'i': movie_id}
        return self._get(params)

    def get_movie_by_title(self, title: str):
        """Retrieve details of a specific movie using its title."""
        params = {'t': title}
        return self._get(params)