## Role of query parameters in this request

In `https://api.github.com/search/repositories`, the query parameters are used by the server to shape what data you want returned. For this request, the important parameters are:

- `q`: the search terms (here, `"python"`) used to filter repositories.
- `sort`: the field to sort by (here, `"stars"`).
- `order`: the sort direction (here, `"desc"` for descending).
- `per_page`: how many results to return per page (here, `5`).

These parameters effectively control filtering, ordering, and limiting at the API side, so the client just receives the already-prepared list.

## Why `response.json()` instead of `response.text()`?

`response.json()` parses the HTTP response body as JSON and converts it into Python data structures (typically `dict` and `list`). That lets you directly access structured fields like `data["items"]` and `repo["stargazers_count"]`.

`response.text()` returns the raw response payload as a plain string. You would then still need to manually parse it (for example with `json.loads`) and then extract the fields yourself. Using `response.json()` is the direct, correct, and more convenient way to work with JSON APIs.
