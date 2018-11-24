# APNG / GIF 생성기

## 주의사항!!!!!!!!!!!!!!!!!!!!!!!!!!!입니다

처음 동영상을 `extract.py`로 추출할 때 디스크에 매우 많은 용량이 필요하니, 동영상 크기는 적절히 넣는 걸 추천합니다.

3분짜리 비트레이트 5534kbps 1280*720 ZxB가 압축 해제하면 5GB 용량을 먹습니다.

아님 압축해제만 다른 걸 쓰던가ㅁ

## 필요 프로그램

apngasm
ffmpeg
pngquant

## 가로영상 자동 회전 기능을 사용할 경우

* opencv 설치

`python -m pip install python-opencv2`로 opencv를 설치합니다.

## 사용 방법

* 폴더 만들기

extract, result 폴더를 만들어줍시다.

* mp4에서 png 추출

동영상 이름을 out.mp4로 변경한 뒤 `python extract.py`를 실행하거나
`python extract.py 파일이름.mp4`를 실행합시다.

* apng 제작

추출이 완료되었으면 만든 `extract` 폴더에서 추출물을 확인합니다.
시작 프레임 번호와 끝 프레임 번호를 잘 관찰한 뒤에

추출한 extract 파일들에서 `assemble.py`을 통해 apng를 만들 수 있습니다.

`python assemble.py`
