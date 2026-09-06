from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates  

app = FastAPI()

templates = Jinja2Templates(directory=templates)

posts: list[dict] = [
    {
        "id": 1,
        "author": "Jackson Mwangi",
        "title": "My First Post",
        "content": "This is my first post on this blog.",
        "date_posted": "2023-06-01"
    },

    {
        "id" : 2,
        "author": "Jane Doe",
        "title": "My Second Post",
        "content": "This is my second post on this blog.",
        "date_posted": "2023-06-02"
    }
]



@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]["title"]}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts