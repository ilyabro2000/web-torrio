import hashlib
import asyncio

import aiohttp_cors  # type: ignore[import]

from aiohttp import web


async def load_torrent(request: web.Request) -> web.Response:
    data = await request.post()
    torrent_file = data["file"]
    return web.json_response({
        "status": "ok",
        "hash": hashlib.sha1(
            torrent_file.file.read()).hexdigest()  # type: ignore[union-attr]
    })


async def state_upload(request: web.Request) -> web.WebSocketResponse:
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    try:
        while True:
            await ws.send_json({"hash": "some_hash"})
            await asyncio.sleep(1)
    finally:
        return ws


app = web.Application()
app.router.add_get("/ws", state_upload)
app.router.add_post("/load_torrent", load_torrent)

cors_options = {
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
}
cors = aiohttp_cors.setup(app, defaults=cors_options)
for route in app.router.routes():
    cors.add(route)


def run() -> None:
    web.run_app(app, host="127.0.0.1", port=5000)
