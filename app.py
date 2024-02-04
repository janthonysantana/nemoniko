from litestar import Litestar, get

@get("/", sync_to_thread=True)
def hello_world() -> dict[str, str]:
    return {"hello": "world"}

app = Litestar(route_handlers=[hello_world])