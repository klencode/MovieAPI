# Movie Scraper

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Movie Scraper** is a python based library for scraping movie data from various sources, designed to help developers easily retrieve details like movie titles, cast, genre, ratings, and more. This library is ideal for projects that require robust movie data without relying on paid APIs.

## Features
- **Scrape movie data**: Retrieve information like title, release date, genre, cast, ratings and summary.
- **Multiple source support**: Connect to various movie databases and websites.
- **Data cleaning and structuring**: Output data in JSON format for easy integration with other applicatins.
- **Rate limiting**: Built-in mechanisms to prevent IP blocking from excessive requests.

## Table of Contents
- [Installations](#installations)
- [Quick Start](#quick-start)
- [Supported Sources](#supported-sources)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure you have Python 3.x or higher installed and the latest version of pip.

Install the library with pip:
```bash
pip install fastapi[standard], dotenv, requests, typing, pydantic
```

## Quick Start

To get started, import the library and use the primary function:

```python
from omdb_client import OMDbClient

# Example usage
result = omdb_client.get_movie_details(movie_id)
print(result)
```

### Example 2: Advanced Usage

For advanced usage, configure the options like so:

```python
from project_name import main_function

result = main_function("advanced input", option1=True, option2=5)
print(result)
```

### Example 3: Saving Output

Since we're working with FastAPI, everything will be web-based (using uvicorn) but you can save the output to a file:

```python
from project_name import main_function
import json

result = main_function("example input")
with open("output.json", "w") as file:
    json.dump(result, file)
```

Or in your terminal, run:
```bash
fastapi dev main.py
```
Open your browser at http://127.0.0.1:8000

## Example Usage:
```
search
    http://127.0.0.1:8000/search/nimona
    
You will see the JSON response as:
{
    "Search": [
        {
            "Title": "Nimona",
            "Year": "2023",
            "imdbID": "tt19500164",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BNTQ2YWZlODctNTJlNS00N2NlLWJlNDktZjM4MmRlYmQ1YWU1XkEyXkFqcGc@._V1_SX300.jpg"
        },]
}
```


## Configuration

You can adjust various settings by passing configuration parameters to the main functions:

```python
config = {
    "option1": True,
    "option2": "value",
}
result = main_function("input", **config)
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue or reach out to me at [ayokwashie42@gmail.com](Klenam Chris).
