import streamlit as st
import requests

st.set_page_config(
    page_title="MoodPick",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    max-width:1200px;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
}

.section-title{
    font-size:26px;
    font-weight:bold;
    margin-top:20px;
}

.poster-card{
    border:1px solid #dddddd;
    border-radius:10px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

movie_images = {
    "인턴": "images/intern.jpg",
    "극한직업": "images/extremejob.jpg",
    "어바웃 타임": "images/abouttime.jpg",
    "월터의 상상은 현실이 된다": "images/walter.jpg",
    "나이브스 아웃": "images/knivesout.jpg"
}

drama_images = {
    "슬기로운 의사생활": "images/hospital.jpg",
    "무빙": "images/moving.jpg",
    "나의 아저씨": "images/myuncle.jpg",
    "선재 업고 튀어": "images/sunjae.jpg",
    "카지노": "images/bigbet.jpg"
}

anime_images = {
    "스파이 패밀리": "images/spyfamily.jpg",
    "바이올렛 에버가든": "images/violet.jpg",
    "원펀맨": "images/onepunch.jpg",
    "너의 이름은": "images/yourname.jpg",
    "진격의 거인": "images/aot.jpg"
}

movie_info = {
    "인턴": {
        "genre": "코미디 · 드라마",
        "plot": "은퇴 후 새로운 직장에 도전하는 시니어 인턴의 성장 이야기"
    },
    "극한직업": {
        "genre": "코미디 · 액션",
        "plot": "치킨집으로 위장 잠입한 형사들의 유쾌한 수사극"
    },
    "어바웃 타임": {
        "genre": "로맨스 · 판타지",
        "plot": "시간을 되돌릴 수 있는 남자의 사랑과 삶에 대한 이야기"
    },
    "월터의 상상은 현실이 된다": {
        "genre": "모험 · 드라마",
        "plot": "평범한 직장인이 진짜 모험을 떠나며 성장하는 이야기"
    },
    "나이브스 아웃": {
        "genre": "미스터리 · 스릴러",
        "plot": "베스트셀러 작가의 죽음을 둘러싼 추리극"
    }
}

drama_info = {
    "슬기로운 의사생활": {
        "genre": "휴먼 · 의학",
        "plot": "20년 지기 의사들의 우정과 일상"
    },
    "무빙": {
        "genre": "액션 · 판타지",
        "plot": "초능력을 가진 가족들의 이야기"
    },
    "나의 아저씨": {
        "genre": "휴먼 · 드라마",
        "plot": "서로 상처를 가진 두 사람이 위로를 주고받는 이야기"
    },
    "선재 업고 튀어": {
        "genre": "로맨스 · 판타지",
        "plot": "과거로 돌아가 첫사랑을 구하려는 청춘 이야기"
    },
    "카지노": {
        "genre": "범죄 · 드라마",
        "plot": "카지노 사업가의 성공과 몰락"
    }
}

anime_info = {
    "스파이 패밀리": {
        "genre": "코미디 · 액션",
        "plot": "각자의 비밀을 가진 가족의 특별한 일상"
    },
    "바이올렛 에버가든": {
        "genre": "드라마",
        "plot": "감정을 배우며 편지를 써주는 소녀"
    },
    "원펀맨": {
        "genre": "액션 · 코미디",
        "plot": "한 방에 모든 적을 쓰러뜨리는 히어로"
    },
    "너의 이름은": {
        "genre": "로맨스 · 판타지",
        "plot": "몸이 뒤바뀌는 두 청춘의 운명적인 만남"
    },
    "진격의 거인": {
        "genre": "액션 · 다크 판타지",
        "plot": "거인에게 맞서는 인류의 생존 이야기"
    }
}

st.image("images/banner.jpg", use_container_width=True)

st.markdown("<div class='main-title'>MoodPick</div>", unsafe_allow_html=True)

st.markdown("""
### 오늘 무엇을 볼지 고민되시나요?

MoodPick은 현재 기분과 상황을 분석하여
사용자에게 가장 어울리는 영화, 드라마, 애니메이션을 추천합니다.

시험기간의 스트레스,
주말의 여유,
설레는 하루,
지친 퇴근 후까지.

지금의 나에게 가장 잘 맞는 콘텐츠를 찾아보세요.
""")

with st.sidebar:

    st.header("MoodPick")

    st.write("Mood & Situation Recommendation")

    st.divider()

    st.write("""
현재 기분과 상황을 기반으로
콘텐츠를 추천하는 서비스입니다.
""")

left, right = st.columns(2)

with left:

    mood = st.radio(
        "현재 기분",
        [
            "행복함",
            "우울함",
            "스트레스 받음",
            "설렘",
            "심심함"
        ]
    )

    companion = st.radio(
        "시청 인원",
        [
            "혼자",
            "친구",
            "연인"
        ]
    )

with right:

    situation = st.selectbox(
        "현재 상황",
        [
            "시험기간",
            "과제 마감 전",
            "주말",
            "방학",
            "퇴근 후"
        ]
    )

    watch_time = st.select_slider(
        "시청 가능 시간",
        options=[
            "30분 이하",
            "1~2시간",
            "정주행 가능"
        ]
    )

recommend = st.button(
    "추천 받기",
    use_container_width=True
)

if recommend:

    with st.spinner("추천 결과 생성 중..."):

        response = requests.post(
            "http://backend:8000/recommend",
            json={
                "mood": mood,
                "situation": situation,
                "watch_time": watch_time,
                "companion": companion
            }
        )

        result = response.json()

    st.markdown("---")

    st.subheader("오늘의 분석 결과")

    st.metric(
        "추천 적합도",
        f"{result['score']}점"
    )

    st.progress(result["score"])

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("현재 기분", mood)

    with c2:
        st.metric("현재 상황", situation)

    with c3:
        st.metric("시청 인원", companion)

    st.markdown("---")

    st.subheader("추천 콘텐츠")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.image(
            movie_images[result["movie"]],
            width=220
        )

        st.markdown(f"### {result['movie']}")

        st.caption(
            movie_info[result["movie"]]["genre"]
        )

        st.write(
            movie_info[result["movie"]]["plot"]
        )

    with col2:

        st.image(
            drama_images[result["drama"]],
            width=220
        )

        st.markdown(f"### {result['drama']}")

        st.caption(
            drama_info[result["drama"]]["genre"]
        )

        st.write(
            drama_info[result["drama"]]["plot"]
        )

    with col3:

        st.image(
            anime_images[result["anime"]],
            width=220
        )

        st.markdown(f"### {result['anime']}")

        st.caption(
            anime_info[result["anime"]]["genre"]
        )

        st.write(
            anime_info[result["anime"]]["plot"]
        )

    st.markdown("---")

    st.subheader("추천 이유")

    st.info(result["reason"])

    st.markdown("""
### 오늘의 시청 팁

- 추천된 작품 중 하나를 선택해 집중해서 시청해보세요.
- 스트레스를 받는 날에는 가벼운 작품부터 시작하는 것을 추천합니다.
- 여유가 있다면 영화와 드라마를 함께 즐겨보세요.
- 혼자 시청할 경우 감성 작품, 친구와 함께라면 코미디 작품을 추천합니다.
""")

st.markdown("---")

st.caption(
    "MoodPick | Open Source Software Practice Final Project"
)