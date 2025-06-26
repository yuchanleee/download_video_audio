```
# How to Download Free Audio / Video

1. 먼저 디렉토리를 만들고 해당 디렉토리로 이동한 뒤, 이 코드를 Git으로 클론하세요.

    git clone https://github.com/your-username/your-repo.git

2. 두 개의 프로그램이 필요합니다:

🟦 yt-dlp  
- 아래 링크에서 `yt-dlp.exe` 파일만 다운로드
  https://github.com/yt-dlp/yt-dlp/releases/latest
- 해당 파일을 방금 만든 디렉토리에 넣으세요

🟦 ffmpeg  
- 아래 링크 접속  
  https://www.gyan.dev/ffmpeg/builds/
- `ffmpeg-release-essentials.zip` 다운로드 후 압축 해제  
- 안에 있는 `bin/ffmpeg.exe`만 디렉토리에 복사

3. 파이썬 코드에서 다음 항목을 **절대경로**로 바꿔주세요:

    save_dir = "C:/yt-dlp/audio"
    cmd = ["C:/yt-dlp/yt-dlp.exe", ...]

4. 실행 방법:
- 첫 줄에 YouTube 링크 붙여넣기
- 두 번째 줄에 저장할 파일 이름 입력
- 오디오/비디오 폴더에 파일 저장됨

Enjoy!
```
