import subprocess, os

url=input().strip()
file_name=input().strip()

save_dir="C:/yt-dlp/video"
save_path=os.path.join(save_dir,file_name)

cmd = [
    "yt-dlp",
    "-f","bv*+ba[ext=m4a]",
    "--merge-output-format","mp4",
    "-o",save_path,
    url
]

subprocess.run(cmd)