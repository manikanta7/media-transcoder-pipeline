from flask import render_template, request
from app import app
import subprocess

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["video"]
        if file:
            filepath = f"./uploads/{file.filename}"
            file.save(filepath)
            subprocess.run(["ffmpeg", "-i", filepath, "-c:v", "libx265", f"./outputs/{file.filename}_hevc.mp4"])
            return "Video uploaded and transcoded to HEVC!"
    return render_template("upload.html")
