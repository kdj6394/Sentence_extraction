# Sentence_extraction

## 개요
[Dacon](https://dacon.io/competitions/official/235671/overview/) 에서 주관하는 한국어 문서 추출요약 AI 경진대회의 데이터를 이용하여 분석을 시도한다.

## 순서
1. 데이터 확인
2. 데이터 분석(https://wikidocs.net/72820)

## reuirements
* pip install -r requiremets.txt
* [KoNLPy](https://konlpy.org/ko/latest/install/)

## Report
### 데이터 확인

* 데이터 구성  

    * train.jsonl - 학습에 사용될 데이터셋  
    1. media : 기사 미디어
    2. id : 각 데이터 고유번호
    3. article_original : 전체 기사 내용, 문장별로 split되어 있음
    4. abstractive : 사람이 생성한 요약문
    5. extractive : 사람이 추출한 요약문 3개의 index
    
    * extractive_test.jsonl - 추론할 데이터셋  
    1. media : 기사 미디어
    2. id : 각 데이터 고유 번호
    3. article_original : 전체 기사 내용, 문장별로 split되어 있음

    * extractive_sample_submission.csv - extractive_test.jsonl의 추론 결과예시  
    1. id : extractive_test.jsonl 데이터의 고유 번호
    2. summary : 모델이 추론한 3개의 추출 문장, 하나의 셀에 각 문장을 로 구분하여 제출