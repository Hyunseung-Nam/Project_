# Notice Alert Bot

경희대학교 채용 공고 게시판을 자동으로 크롤링하여 **신규 공지**가 등록되면 Gmail로 알림을 보내주는 프로그램입니다.  
**이 프로젝트는 학습 및 포트폴리오 용도로만 제작되었으며, 실제 운영이나 상업적 사용을 목적으로 하지 않습니다.**

## ✨ 기능

- 경희대 채용 게시판 1페이지 크롤링
- 기존 공고와 비교하여 **신규 공지**만 탐지
- 신규 공지를 **Gmail 메일 알림**으로 발송
- CSV 파일에 공고 기록 저장
- 실행 로그(posts.log) 저장

---

## ⚙️ 기술 스택

- Python 3.13
- requests
- pandas  
- python-dotenv
- logging

---

## 🚀 설치 & 실행 방법

```bash
1. 레포지토리 복사
git clone https://github.com/Hyunseung-Nam/Project_.git
cd Project_

2. 라이브러리 설치
pip install -r requirements.txt

3. 환경변수 설정 (.env 파일 생성)
echo "NAVER_CLIENT_ID=your_client_id" >> .env
echo "NAVER_CLIENT_SECRET=your_client_secret" >> .env

4. 실행
python main.py
```

---


## 📝 로깅

- 실행 로그가 **`posts.log`** 파일에 저장됩니다.    
- 로그에 기록되는 내용:  
  - 수집된 게시물 개수  
  - 신규 공고 개수  
  - 메일 발송 성공/실패 여부

---

## 🔐 Gmail 설정 주의

- Gmail SMTP를 사용하려면 **앱 비밀번호(App Password)** 가 필요합니다.  
- Gmail 계정에서 **2단계 인증**을 활성화한 뒤, 앱 비밀번호를 발급받아 `.env`의 `SMTP_PASS`에 입력하세요.  