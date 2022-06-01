# Simple .Minecraft File Installer 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdlams%2Fsimple_installer%2F&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=github&edge_flat=false)](https://hits.seeyoufarm.com) 마인크래프트 간편설치기 데모 버전 프로젝트입니다 

## 시작하기

### PYTHON 설치
  우선 파이썬을 설치해야합니다.
  기본적으로는 [파이썬](https://www.python.org/)에서 받을 수 있지만, 
파이썬을 한번도 해본적이 없는 분들은 [파이참](https://www.jetbrains.com/ko-kr/pycharm/download/)에서 IDE를 받아봅시다
 > Community 버전으로 받으셔야 무료입니다

<br>

### 프로젝트 생성
New Project 버튼을 눌러 새로운 프로젝트를 만듭니다.

잠시 후 설정한 이름에 해당하는 위치에 프로젝트가 생성되고 main.py하나가 생성되어 있습니다    

<br>

### pyinstaller 설치
Alt + F12나 하단에 Terminal에서 pyinstaller를 설치합니다
```
pip install pyinstaller
```

<br>

### main.py에 코드 넣기
본 페이지에 [main.py](https://github.com/dlams/simple_installer/blob/main/main.py)에 있는 소스코드를 프로젝트 내 main.py에 붙여 넣습니다.

<br>

### resource 폴더 생성 및 파일 추가
프로젝트 안에 있는 main.py와 같은 위치에 resource 폴더를 하나 생성해 주고 안에 구성 파일들을 넣어줍니다.
 - `bg.png` : 950 x 600 크기의 사진으로써 GUI에 배경이 되는 부분  
 - `bg_install` : bg.png와 같은 서식의 PNG로 설치중 바뀌는 부분  
 - `btn.png` : 설치 버튼의 사진으로 사이즈는 439 x 58  
 - `icon.ico` : 프로그램 아이콘  
 - `target.zip` : .minecraft 폴더에 추가할 파일 (압축해제 방식)  

## 배포하기
### 실행파일 만들기
위 방법이 모두 끝났다면 실행파일을 만들어봅시다.  
다시 터미널 창으로 돌아가 아래 코드를 입력해 줍니다
```
pyinstaller -w -F --icon="resource/icon.ico" --add-data="resource/*;resource" main.py
```
실행이 완료되면 폴더내 dist 폴더에 실행 파일이 만들어 나옵니다

<br>

### 배포하기
모두 끝났습니다. 이제 만들어진 파일을 공유하기만 합니다.  
공유된 파일이 바이러스로 인식된다면 구글드라이브를 통해 공유를 진행해 보시기 바랍니다.


## 주의
1. 대중적인 방법이 아닌 많은 사람들이 쉽게 사용하라고 만든 코드입니다  
2. target.zip 폴더 안 파일에 한글 이름이 있을 경우 이름이 깨지게 됩니다(내용은 괜찮습니다)
3. (중요!) 배포 권리가 있는 저작물만 설치기에 포함하고 이를 다운받은 사람들이 볼 수 있도록 명시해주세요
