import requests


def search_repositories(query: str = "python", limit: int = 5) -> None:
    """
    Search GitHub repositories by query, sorted by stars (descending),
    and print the top `limit` repository names and star counts.
    """
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit,
    }
    headers = {
        # Request a predictable JSON media type.
        "Accept": "application/vnd.github+json",
    }

    response = requests.get(url, params=params, headers=headers, timeout=15)
    response.raise_for_status()
    data = response.json()

    for repo in data.get("items", [])[:limit]:
        name = repo.get("name")
        stars = repo.get("stargazers_count")
        print(f"{name} {stars}")


if __name__ == "__main__":
    search_repositories()
