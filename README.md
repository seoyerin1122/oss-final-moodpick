# MoodPick 

Streamlit + FastAPI + Docker + AWS EC2 기반 콘텐츠 추천 웹 애플리케이션

## 프로젝트 소개

MoodPick은 사용자의 현재 기분과 상황을 입력받아 영화, 드라마, 애니메이션을 추천해주는 웹 서비스입니다.

사용자가 Streamlit 화면에서 정보를 입력하면 FastAPI 서버가 추천 결과를 생성하고, 결과를 다시 Streamlit 화면에 표시합니다.

---

## 사용 기술

* Streamlit
* FastAPI
* Docker
* AWS EC2
* Python

---

## 시스템 구조

사용자 입력 → Streamlit → FastAPI → 추천 결과 반환 → Streamlit 출력

---

## 입력 항목

* 현재 기분
* 현재 상황
* 시청 가능 시간
* 함께 보는 사람

---

## 출력 결과

* 영화 추천
* 드라마 추천
* 애니메이션 추천
* 추천 이유
* 추천 적합도 점수

---

## 프로젝트 구조

```
oss-final-moodpick

├── front
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile

├── back
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile

├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 실행 방법

### Backend

```bash
docker build -t moodpick-back ./back
docker run -d --name moodpick-back -p 8000:8000 moodpick-back
```

### Frontend

```bash
docker build -t moodpick-front ./front
docker run -d --name moodpick-front -p 8501:8501 moodpick-front
```

---

## 서비스 접속

```
http://EC2_PUBLIC_IP:8501
```

---

## 주요 기능

* 사용자 입력 기반 콘텐츠 추천
* Streamlit과 FastAPI 간 HTTP 통신
* Docker 컨테이너 기반 실행 환경
* AWS EC2 서버 배포

---

## 개발자

오픈소스소프트웨어실습 기말 대체 과제
