from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse

from commom import (
    get_meeting_name,
    get_meeting_response,
    mattermost_command_to_json,
)
from settings import GOOGLE_MEET_URL, MATTERMOST_TOKEN


app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/")
async def main(request: Request):
    bytes_body = await request.body()
    body = mattermost_command_to_json(str(bytes_body))

    if body["token"] == MATTERMOST_TOKEN:
        user_mentions = [f"@{user}" for user in body["user_mentions"]]

        return {
            "response_type": "in_channel",
            "text": get_meeting_response(
                user_mentions,
                f"{GOOGLE_MEET_URL}{get_meeting_name(body['text'])}",
            ),
            "username": "google-meet",
            "attachments": [{"image_url": f"{str(request.url)}image"}],
        }
    return Response(status_code=401)


@app.get("/icon")
async def google_meet_icon():
    return FileResponse("icons/blue_icon.png")


@app.get("/image")
async def meeting_image():
    return FileResponse("icons/emergency_meeting.png")
