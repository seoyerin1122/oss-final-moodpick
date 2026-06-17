from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


class UserInput(BaseModel):
    mood: str
    situation: str
    watch_time: str
    companion: str


@app.post("/recommend")
def recommend(data: UserInput):

    if data.mood == "스트레스 받음" and data.situation == "시험기간":

        movie = "인턴"
        drama = "무빙"
        anime = "원펀맨"

        reason = (
            "시험으로 인한 스트레스를 해소할 수 있는 "
            "가볍고 몰입감 있는 작품을 추천합니다."
        )

    elif data.mood == "우울함":

        movie = "월터의 상상은 현실이 된다"
        drama = "나의 아저씨"
        anime = "바이올렛 에버가든"

        reason = (
            "위로와 공감을 얻을 수 있는 작품을 추천합니다."
        )

    elif data.mood == "행복함":

        movie = "극한직업"
        drama = "슬기로운 의사생활"
        anime = "스파이 패밀리"

        reason = (
            "현재 기분을 유지하며 즐겁게 볼 수 있는 작품입니다."
        )

    elif data.mood == "설렘":

        movie = "어바웃 타임"
        drama = "선재 업고 튀어"
        anime = "너의 이름은"

        reason = (
            "감성적이고 설레는 분위기의 작품을 추천합니다."
        )

    else:

        movie = "나이브스 아웃"
        drama = "카지노"
        anime = "진격의 거인"

        reason = (
            "지루함을 잊을 수 있도록 몰입감 있는 작품을 추천합니다."
        )

    score = random.randint(78, 98)

    return {
        "movie": movie,
        "drama": drama,
        "anime": anime,
        "reason": reason,
        "score": score
    }