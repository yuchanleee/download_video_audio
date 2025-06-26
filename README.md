# 🎵 How to Download Free Audio / Video

1. 먼저 디렉토리를 하나 만들고, 그 안에서 이 코드를 클론하세요:

    git clone https://github.com/your-username/your-repo.git

2. 아래 두 프로그램을 설치해야 합니다:

▶ **yt-dlp**  
- 다운로드 링크: [yt-dlp 다운로드](https://github.com/yt-dlp/yt-dlp/releases/latest)  
- `yt-dlp.exe` 하나만 다운받아서 위에서 만든 폴더에 넣으세요

▶ **ffmpeg**  
- 다운로드 링크: [ffmpeg 다운로드](https://www.gyan.dev/ffmpeg/builds/)  
- 페이지에서 `ffmpeg-release-essentials.zip`을 다운로드  
- 압축 해제 후 `bin/ffmpeg.exe` 파일만 꺼내서 폴더에 넣으세요

    예시 구조:
    ```
    C:/yt-dlp/
    ├── yt-dlp.exe
    └── ffmpeg.exe
    ```

3. 파이썬 코드에서 다음 경로들을 **절대경로로 수정**하세요:

    save_dir = "C:/yt-dlp/audio"  
    cmd = ["C:/yt-dlp/yt-dlp.exe", ...]

4. 실행 방법:
- 첫 줄에 YouTube 링크 입력  
- 두 번째 줄에 저장할 파일명 입력  
- 오디오/영상이 audio/ 또는 video/ 폴더에 저장됩니다

✅ 모든 준비가 끝났다면 코드를 실행하세요!
