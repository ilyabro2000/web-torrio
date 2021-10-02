from aiohttp import web


async def load_torrent(request: web.Request) -> web.Response:
    print(request.headers)
    data = await request.post()
    torrent_file_data = data["torrent_file"]
    return web.json_response({
        "status": "ok",
        "filename": torrent_file_data.filename,  # type: ignore [union-attr]
        "length": len(torrent_file_data.file.read())  # type:  ignore [union-attr]
    })


app = web.Application()

app.add_routes([
    web.post("/load_torrent", load_torrent)
])


def run() -> None:
    web.run_app(app, host="127.0.0.1", port=5000)
