# NERI · Streamlit
현재 NERI의 배경·소리·파도·배 배치·모래 글씨 기능을 그대로 내장한 Streamlit 실행판입니다. 외부 Sites 주소나 API 키 없이 작동합니다.

## GitHub → Streamlit 배포
1. GitHub에서 새 저장소를 만듭니다(예: neri-beach).
2. ZIP을 풀고 이 폴더 안의 app.py, requirements.txt, beach.html, .streamlit 폴더를 저장소 최상위에 올립니다. ZIP 자체를 올리지 마세요.
3. https://share.streamlit.io 에 GitHub 계정으로 로그인하고 Create app을 누릅니다.
4. 저장소와 main 브랜치를 선택하고 Main file path를 app.py로 지정해 Deploy합니다.

## 로컬 실행
python -m pip install -r requirements.txt
python -m streamlit run app.py

## 조작
아이콘 선택 후 원하는 바다/하늘 위치를 누르면 물체가 하나씩 추가됩니다.
✎ 모래 글씨를 누르면 모래에 손글씨와 그림을 그릴 수 있습니다. 같은 버튼을 다시 누르면 해제됩니다.
굵기·한 획 취소·지우기를 지원하며 ✋로 풍경을 둘러봅니다.
소리는 재생 버튼을 눌러 시작합니다.
배치·글씨는 같은 브라우저에 저장됩니다. 배포 주소가 달라지면 기존 주소의 기록은 자동 이전되지 않습니다.
Streamlit은 기존 HTML/JS를 iframe 안에서 실행합니다. 풍경과 상호작용은 동일한 소스이며 전체화면 동작은 브라우저의 iframe 정책에 따라 달라질 수 있습니다.

beach.html에는 이미지·CSS·JavaScript가 모두 내장되어 있습니다. 원본 편집용 소스는 기존 NERI_wide_app_and_code.zip의 source 폴더에 있습니다.
