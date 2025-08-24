## 📰 네이버 뉴스 검색기 (Naver News Searcher)

네이버 **오픈 API**를 활용하여 원하는 키워드의 뉴스를 검색하고,  
그 결과를 **CSV 파일로 저장**할 수 있는 GUI 프로그램입니다. 
**이 프로젝트는 학습 및 포트폴리오 용도로만 제작되었으며, 실제 운영이나 상업적 사용을 목적으로 하지 않습니다.**

## ✨ 기능

- 검색어 입력 후 버튼 클릭으로 네이버 뉴스 검색
- 결과 개수 지정 (최소 10개)
- 정렬 기준 선택 (정확도순 / 날짜순)
- 검색 결과를 News_data_YYYYMMDD_HH시MM분.csv 형식으로 자동 저장
- 실행 로그(news_search.log) 저장

---

## ⚙️ 기술 스택

- Python 3.13
- requests
- pandas  
- python-dotenv
- PySide6
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
python src/app.py
```

---


## 📝 로그(logging)

- 실행 로그가 **`news_search.log`** 파일에 저장됩니다.    
- 로그에 기록되는 내용:  
  - 검색어
  - 요청 성공/실패 여부
  - 검색 결과 개수
  - 저장된 CSV 파일명

---