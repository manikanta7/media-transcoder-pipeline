# Media Transcoder Pipeline 🎬

A lightweight, containerized media ingestion and encoding system that processes user-uploaded videos using **FFMPEG**, supports encoding in **AV1, HEVC (H.265)**, and stores metadata in MongoDB. The project is built with **Python Flask**, **Docker**, and integrates with **AWS S3 + CloudFront** for delivery.

## 🚀 Features
- Upload video files via web interface
- Transcode videos to multiple formats (AV1, HEVC, H.264)
- Extract and store video metadata (resolution, duration, codec)
- Store encoded files in AWS S3
- Serve via CloudFront for global delivery
- Fully Dockerized setup with CI/CD potential
- Configurable with `.env` for environment separation

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Encoding:** FFMPEG
- **Database:** MongoDB
- **Cloud:** AWS S3, CloudFront
- **Containerization:** Docker
- **Frontend:** HTML + Bootstrap

## 🧪 How to Run
```bash
git clone https://github.com/YOUR_USERNAME/media-transcoder-pipeline.git
cd media-transcoder-pipeline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## 🐳 Docker Support
```bash
docker build -t media-transcoder .
docker run -p 5000:5000 --env-file .env media-transcoder
```

## ⚙️ Encoding Sample
```bash
ffmpeg -i input.mp4 -c:v libaom-av1 output_av1.mkv
ffmpeg -i input.mp4 -c:v libx265 output_hevc.mp4
```

## 🧠 Metadata Example
```json
{
  "filename": "demo.mp4",
  "codec": "H.264",
  "duration": "00:02:34",
  "resolutions": ["1920x1080", "1280x720"],
  "formats": ["AV1", "HEVC", "H.264"]
}
```

## 👤 Author
**Chowdary Manikanta Yarramaneni**
[LinkedIn](https://www.linkedin.com/in/chowdary-manikanta/) | [Portfolio](https://manikanta7.github.io/Chowdaryportfolio.github.io/) | [Email](mailto:chowdaryy25@gmail.com)
