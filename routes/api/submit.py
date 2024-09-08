from fastapi import APIRouter, FastAPI, Response, Form, Query, UploadFile, File
import utils
app = APIRouter(
)

@app.post("/api/submit.php")
async def PreSubmit(userID: str = Form(...), playID: str = Form(None), ssid: str = Form(None), filename: str = Form(None), hash: str = Form(None), songTitle: str = Form(None), songArtist: str = Form(None), songCreator: str = Form(None), data: str = Form(None), sign: str = Form(None), replayFileChecksum: str = Form(None), replayFile: UploadFile = File(None)):
    if ssid and filename and hash and songTitle and songArtist and songCreator:
        print(f"Play started by {userID} ({ssid})")
        return Response(utils.generate_play(userID, ssid, filename, hash, songTitle, songArtist, songCreator))
    elif playID and data and sign and replayFileChecksum:
        print(f"Play submitted by {userID}")
        with open(f'replays/{replayFile.filename}', "wb") as f:
            f.write(await replayFile.read())
        return Response(utils.get_play_response(playID,data,userID))