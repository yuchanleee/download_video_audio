import subprocess, os

url=input().strip()
file_name=input().strip()

save_dir="C:/yt-dlp/audio"
save_path=os.path.join(save_dir,file_name)

yt_dlp_cmd = [
    "C:/yt-dlp/yt-dlp.exe",
    "-f","bestaudio",
    "--extract-audio",
    "--audio-format","wav",
    "--audio-quality","0",
    "-o",save_path,
    url
]

subprocess.run(yt_dlp_cmd)
