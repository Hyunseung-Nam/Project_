# **네이버 오픈 API를 이용해 뉴스를 검색해주는 프로그램 개발**
# **API키 필요**
import requests, re, os
import pandas as pd
from dotenv import load_dotenv
from urllib.parse import urlencode
import logging

load_dotenv()  # .env 파일 불러오기

# ===================
# 로그 설정
# ===================

logging.basicConfig(
    level=logging.INFO,                         
    format='%(asctime)s %(levelname)-8s %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S',                
    filename='news_search.log',                       
    filemode='a'                                
)
logger = logging.getLogger(__name__)



# HTML 태그 제거 함수 정의
def remove_html_tags(text):
    return re.sub(r'<[^>]*>', '', text)


def search_news(query, display, sort):
    sort_map = {"sim": "정확도순", "date": "날짜순"}
    logger.info(f"뉴스 검색 시작 | query={query}, display={display}, sort={sort_map.get(sort, sort)}")
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise ValueError("API 키가 없습니다. .env 파일을 확인하세요.")
    
    params = {"query": query, "display": display, "sort": sort}
    naver_open_api = f"https://openapi.naver.com/v1/search/news.json?{urlencode(params)}"
    header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    try:
        res = requests.get(naver_open_api, headers=header_params, timeout=10)
        res.raise_for_status()
        logger.info("API 요청 성공")
    except requests.exceptions.RequestException as e:
        print(f"요청 실패: {e}")
        logger.error(f"API 요청 실패: {e}")
        return None

    datas=[]

    api_data = res.json()
    for item in api_data['items']:
        datas.append({"제목": remove_html_tags(item['title']), "링크": item['link']}) # HTML 태그 제거

    # csv 파일에 저장
    df = pd.DataFrame(data=datas)
    now = pd.Timestamp.now()
    timestamp_str = f"{now.strftime('%Y%m%d')}_{now.hour:02d}시{now.minute:02d}분"
    filename = f'News_data_{timestamp_str}.csv'
    df.to_csv(filename, encoding="utf-8-sig", index=True)
    logger.info(f"검색 결과 {len(datas)}건 저장 완료 → {filename}")
    
    return filename