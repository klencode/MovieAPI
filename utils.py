from fastapi import HTTPException

def handle_api_error(response_data):
    """Raise an HTTPException if the API response contains an error."""
    if "error" in response_data:
        raise HTTPException(status_code=404, detail="Resource not found")