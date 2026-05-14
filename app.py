import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 & 포켓몬 추천기",
    page_icon="🎯",
    layout="centered"
)

st.title("✨ MBTI 진로 & 포켓몬 추천기")
st.markdown("## 🎯 나의 MBTI에 어울리는 진로와 포켓몬은?!")
st.write("MBTI를 선택하면 추천 진로 + 닮은 포켓몬까지 알려줄게 😆")

# -----------------------------
# MBTI 데이터
# -----------------------------
mbti_data = {
    "INTJ": {
        "careers": [
            {"career": "🧠 데이터 사이언티스트", "major": "컴퓨터공학과, 통계학과", "personality": "논리적이고 분석을 좋아하는 사람!"},
            {"career": "🏗️ 건축가", "major": "건축학과", "personality": "계획 세우고 전략적으로 움직이는 스타일!"}
        ],
        "pokemon": {
            "name": "뮤츠",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
            "desc": "🧠 천재적이고 전략적인 모습이 INTJ와 닮았어!"
        }
    },

    "INTP": {
        "careers": [
            {"career": "💻 프로그래머", "major": "소프트웨어학과", "personality": "호기심 많고 탐구를 좋아함!"},
            {"career": "🔬 연구원", "major": "물리학과, 화학과", "personality": "깊게 파고드는 걸 잘하는 스타일!"}
        ],
        "pokemon": {
            "name": "후딘",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
            "desc": "📚 높은 지능과 분석력이 INTP 느낌이야!"
        }
    },

    "ENTJ": {
        "careers": [
            {"career": "📈 CEO", "major": "경영학과", "personality": "리더십 있고 추진력이 강함!"},
            {"career": "⚖️ 변호사", "major": "법학과", "personality": "설득력 있고 논리적인 사람!"}
        ],
        "pokemon": {
            "name": "리자몽",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
            "desc": "🔥 카리스마 넘치는 리더형 포켓몬!"
        }
    },

    "ENTP": {
        "careers": [
            {"career": "🎤 마케터", "major": "광고홍보학과", "personality": "아이디어 넘치고 소통을 좋아함!"},
            {"career": "🚀 창업가", "major": "경영학과", "personality": "새로운 도전을 즐김!"}
        ],
        "pokemon": {
            "name": "팬텀",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
            "desc": "😎 장난기 많고 창의적인 ENTP와 찰떡!"
        }
    },

    "INFJ": {
        "careers": [
            {"career": "💖 상담사", "major": "심리학과", "personality": "공감 능력이 뛰어남!"},
            {"career": "✍️ 작가", "major": "문예창작과", "personality": "감수성이 풍부한 스타일!"}
        ],
        "pokemon": {
            "name": "루기아",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
            "desc": "🌊 신비롭고 깊은 분위기가 INFJ 같아!"
        }
    },

    "INFP": {
        "careers": [
            {"career": "🎨 일러스트레이터", "major": "디자인학과", "personality": "감성적이고 창의력이 풍부함!"},
            {"career": "🎵 음악 프로듀서", "major": "실용음악과", "personality": "자신만의 감성을 표현하는 걸 좋아함!"}
        ],
        "pokemon": {
            "name": "이브이",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
            "desc": "🌈 가능성이 무한한 포켓몬!"
        }
    },

    "ENFJ": {
        "careers": [
            {"career": "👩‍🏫 교사", "major": "교육학과", "personality": "사람들을 잘 이끌고 도와줌!"},
            {"career": "🎙️ 아나운서", "major": "미디어커뮤니케이션학과", "personality": "밝고 긍정적인 에너지!"}
        ],
        "pokemon": {
            "name": "피카츄",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "desc": "⚡ 모두에게 사랑받는 따뜻한 성격!"
        }
    },

    "ENFP": {
        "careers": [
            {"career": "📹 유튜버", "major": "영상학과", "personality": "끼 많고 자유로운 스타일!"},
            {"career": "🌏 여행 콘텐츠 제작자", "major": "관광학과", "personality": "새로운 경험을 좋아함!"}
        ],
        "pokemon": {
            "name": "파이리",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
            "desc": "🔥 열정 넘치고 에너지 가득!"
        }
    },

    "ISTJ": {
        "careers": [
            {"career": "🏦 회계사", "major": "세무회계학과", "personality": "꼼꼼하고 책임감이 강함!"},
            {"career": "👮 경찰관", "major": "경찰행정학과", "personality": "원칙을 중요하게 생각함!"}
        ],
        "pokemon": {
            "name": "거북왕",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
            "desc": "🛡️ 듬직하고 믿음직한 모습이 ISTJ 느낌!"
        }
    },

    "ISFJ": {
        "careers": [
            {"career": "🩺 간호사", "major": "간호학과", "personality": "배려심 많고 따뜻함!"},
            {"career": "🏫 사회복지사", "major": "사회복지학과", "personality": "사람들을 잘 챙김!"}
        ],
        "pokemon": {
            "name": "해피너스",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
            "desc": "💖 치유와 배려의 상징 같은 포켓몬!"
        }
    },

    "ESTJ": {
        "careers": [
            {"career": "📊 공무원", "major": "행정학과", "personality": "체계적이고 리더십 있음!"},
            {"career": "🏢 기업 관리자", "major": "경영학과", "personality": "조직 관리에 강함!"}
        ],
        "pokemon": {
            "name": "보스로라",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/306.png",
            "desc": "⛰️ 강인하고 책임감 있는 모습!"
        }
    },

    "ESFJ": {
        "careers": [
            {"career": "🎉 행사 기획자", "major": "이벤트학과", "personality": "사람들과 어울리는 걸 좋아함!"},
            {"career": "🧑‍⚕️ 병원 코디네이터", "major": "보건행정학과", "personality": "친절하고 배려심 많음!"}
        ],
        "pokemon": {
            "name": "푸크린",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png",
            "desc": "🎵 밝고 사랑스러운 분위기의 포켓몬!"
        }
    },

    "ISTP": {
        "careers": [
            {"career": "🔧 엔지니어", "major": "기계공학과", "personality": "직접 만들고 해결하는 걸 좋아함!"},
            {"career": "🏍️ 자동차 정비사", "major": "자동차학과", "personality": "실전형 문제 해결사!"}
        ],
        "pokemon": {
            "name": "핫삼",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png",
            "desc": "⚙️ 냉철하고 실전 능력이 뛰어난 느낌!"
        }
    },

    "ISFP": {
        "careers": [
            {"career": "📷 사진작가", "major": "사진영상학과", "personality": "감각적이고 자유로움!"},
            {"career": "💄 메이크업 아티스트", "major": "뷰티학과", "personality": "예술 감각이 뛰어남!"}
        ],
        "pokemon": {
            "name": "세레비",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/251.png",
            "desc": "🌿 조용하고 따뜻한 감성의 포켓몬!"
        }
    },

    "ESTP": {
        "careers": [
            {"career": "🏀 스포츠 트레이너", "major": "체육학과", "personality": "활동적이고 에너지가 넘침!"},
            {"career": "💼 영업 전문가", "major": "마케팅학과", "personality": "사람들과 금방 친해짐!"}
        ],
        "pokemon": {
            "name": "번치코",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png",
            "desc": "🔥 승부욕 넘치고 활동적인 스타일!"
        }
    },

    "ESFP": {
        "careers": [
            {"career": "🎬 배우", "major": "연극영화과", "personality": "표현력이 풍부하고 밝음!"},
            {"career": "🎤 아이돌 트레이너", "major": "실용무용과", "personality": "끼 많고 주목받는 걸 좋아함!"}
        ],
        "pokemon": {
            "name": "푸린",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
            "desc": "🎤 사랑스럽고 분위기 메이커 느낌!"
        }
    }
}

# -----------------------------
# MBTI 선택
# -----------------------------
selected_mbti = st.selectbox(
    "💡 너의 MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# -----------------------------
# 결과 버튼
# -----------------------------
if st.button("🎁 결과 확인하기"):

    st.success(f"✨ {selected_mbti} 유형 결과가 나왔어!")

    # 진로 추천
    st.header("🎯 추천 진로")

    careers = mbti_data[selected_mbti]["careers"]

    for idx, item in enumerate(careers, start=1):
        st.subheader(f"{idx}. {item['career']}")
        st.write(f"🎓 추천 학과 : **{item['major']}**")
        st.write(f"💖 어울리는 성격 : {item['personality']}")
        st.markdown("---")

    # 포켓몬 추천
    pokemon = mbti_data[selected_mbti]["pokemon"]

    st.header("⚡ 너와 닮은 포켓몬!")

    st.image(pokemon["image"], width=200)

    st.subheader(f"🧩 {pokemon['name']}")
    st.write(pokemon["desc"])

    st.info("🌟 포켓몬처럼 너만의 매력을 멋지게 살려보자!")

    st.balloons()

# -----------------------------
# 하단 문구
# -----------------------------
st.caption("🌈 MBTI와 포켓몬 추천은 재미로 즐겨줘 😆")
