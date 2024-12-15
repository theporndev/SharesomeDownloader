from flask import Flask, render_template, request, Response, stream_with_context
from main import get_video_url
import asyncio
import requests

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/get_video", methods=["POST"])
def api_get_video_url():
    payload = request.get_json()
     # {'url': 'https://sharesome.com/MinnieQuinn/post/c9b9c74b-fb0d-4c0d-a820-5791ac773c0a'}
    post_url = payload['url']
    video_url = asyncio.run(get_video_url(post_url))
    return {"video_url": video_url}

@app.route("/video_relay/<path:path>")
def video_relay(path):
    video_url = path  # External video URL

    range_header = request.headers.get("Range", None)
    headers = {}

    if range_header:
        # Forward the Range header to the external server
        headers["Range"] = range_header

    # Request the video content from the external URL
    upstream_response = requests.get(video_url, stream=True, headers=headers)

    # Prepare Flask response
    response = Response(
        stream_with_context(upstream_response.iter_content(chunk_size=1024)),
        status=upstream_response.status_code,
        content_type=upstream_response.headers.get("Content-Type"),
    )

    # Pass through headers related to content range
    response.headers["Content-Range"] = upstream_response.headers.get("Content-Range", "")
    response.headers["Accept-Ranges"] = "bytes"
    response.headers["Content-Length"] = upstream_response.headers.get("Content-Length", "")

    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")