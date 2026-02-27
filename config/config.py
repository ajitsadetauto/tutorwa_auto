import os

class Config:
    RECORD_VIDEO = os.getenv("RECORD_VIDEO", "false").lower() == "true"
    VIDEO_DIR = "videos/"