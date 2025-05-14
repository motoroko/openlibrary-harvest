import subprocess
import json
from typing import List, Dict
from tqdm import tqdm
import os

def fetch_genres_playwright(isbn: str, script_path: str = None) -> Dict:
    if script_path is None:
        script_path = os.path.join(os.path.dirname(__file__), "..", "scrape_openlibrary.js")
    try:
        result = subprocess.run(
            ["node", script_path, isbn],
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            return {"isbn": isbn, "genres": [], "error": result.stderr.strip()}
    except Exception as e:
        return {"isbn": isbn, "genres": [], "error": str(e)}

def openlibrary_harvest(isbn_list: List[str], script_path: str = None, show_progress=True) -> List[Dict]:
    results = []
    iterator = tqdm(isbn_list, desc="Scraping OpenLibrary") if show_progress else isbn_list

    for isbn in iterator:
        data = fetch_genres_playwright(isbn, script_path)
        results.append(data)

    return results
