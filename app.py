import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 & 포켓몬 추천기",
    page_icon="🎯",
    layout="centered"
)

st.title("✨ MBTI 진로 & 포켓몬 추천기")
st.markdown("## 🎯 나의 MBTI에 어울리는 진로와 포켓몬은?!")
st.write("MBTI를 선택하면 진로 추천 + 닮은 포켓몬까지 알려줄게 😆")

# -----------------------------
# MBTI 데이터
# -----------------------------
mbti_data = {
    "INTJ": {
        "careers": [
            {
                "career": "🧠 데이터 사이언티스트",
                "major": "컴퓨터공학과, 통계학과",
                "personality": "논리적이고 분석을 좋아하는 사람!"
            },
            {
                "career": "🏗️ 건축가",
                "major": "건축학과",
                "personality": "창의적이면서 계획 세우는 걸 좋아하는 스타일!"
            }
        ],
        "pokemon": {
            "name": "뮤츠",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
            "desc": "🧠 천재적이고 전략적인 성격! 혼자 깊게 생각하는 모습이 INTJ와 닮았어."
        }
    },

    "INTP": {
        "careers": [
            {
                "career": "💻 프로그래머",
                "major": "소프트웨어학과",
                "personality": "호기심 많고 새로운 아이디어를 좋아함!"
            },
            {
                "career": "🔬 연구원",
                "major": "물리학과, 화학과",
                "personality": "깊게 탐구하고 혼자 집중하는 걸 잘함!"
            }
        ],
        "pokemon": {
            "name": "후딘",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
            "desc": "📚 높은 지능과 탐구심이 특징! 분석적인 INTP와 찰떡!"
        }
    },

    "ENTJ": {
        "careers": [
            {
                "career": "📈 CEO",
                "major": "경영학과",
                "personality": "리더십 있고 목표 지향적인 타입!"
            },
            {
                "career": "⚖️ 변호사",
                "major": "법학과",
                "personality": "논리적이고 설득력이 강함!"
            }
        ],
        "pokemon": {
            "name": "리자몽",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
            "desc": "🔥 강한 카리스마와 리더 기질! ENTJ의 자신감과 닮았어."
        }
    },

    "ENTP": {
        "careers": [
            {
                "career": "🎤 마케터",
                "major": "광고홍보학과",
                "personality": "아이디어 많고 소통을 좋아함!"
            },
            {
                "career": "🚀 창업가",
                "major": "경영학과",
                "personality": "도전을 즐기는 혁신가 스타일!"
            }
        ],
        "pokemon": {
            "name": "팬텀",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
            "desc": "😎 장난기 많고 창의적인 성격! 자유로운 ENTP 느낌!"
        }
    },

    "INFJ": {
        "careers": [
            {
                "career": "💖 상담사",
                "major": "심리학과",
                "personality": "공감 능력이 뛰어난 사람!"
            },
            {
                "career": "✍️ 작가",
                "major": "문예창작과",
                "personality": "감수성이 풍부하고 상상력이 뛰어남!"
            }
        ],
        "pokemon": {
            "name": "루기아",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
            "desc": "🌊 신비롭고 깊은 내면을 가진 포켓몬! INFJ와 정말 잘 어울려."
        }
    },

    "INFP": {
        "careers": [
            {
                "career": "🎨 일러스트레이터",
                "major": "디자인학과",
                "personality": "감성적이고 창의력이 풍부함!"
            },
            {
                "career": "🎵 음악 프로듀서",
                "major": "실용음악과",
                "personality": "자신만의 감성을 표현하는 걸 좋아함!"
            }
        ],
        "pokemon": {
            "name": "이브이",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
            "desc": "🌈 가능성이 무한한 포켓몬! 따뜻하고 감성적인 INFP와 닮았어."
        }
    },

    "ENFJ": {
        "careers": [
            {
                "career": "👩‍🏫 교사",
                "major": "교육학과",
                "personality": "사람들을 도와주고 이끄는 걸 좋아함!"
            },
            {
                "career": "🎙️ 아나운서",
                "major": "미디어커뮤니케이션학과",
                "personality": "밝고 긍정적인 에너지가 넘침!"
            }
        ],
        "pokemon": {
            "name": "피카츄",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "desc": "⚡ 밝고 모두에게 사랑받는 성격! ENFJ의 따뜻함과 닮았어."
        }
    },

    "ENFP": {
        "careers": [
            {
                "career": "📹 유튜버",
                "major": "영상학과",
                "personality": "끼 많고 자유로운 스타일!"
            },
            {
                "career": "🌏 여행 콘텐츠 제작자",
                "major": "관광학과",
                "personality": "새로운 경험을 좋아함!"
            }
        ],
        "pokemon": {
            "name": "파이리",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
            "desc": "🔥 열정 넘치고 에너지가 가득! ENFP 느낌 뿜뿜!"
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
# 버튼 클릭
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

    st.info("🌟 포켓몬처럼 너만의 매력을 살려보자!")

    st.balloons()

# -----------------------------
# 하단 문구
# -----------------------------
st.caption("🌈 MBTI와 포켓몬 추천은 재미로 즐겨줘 😆")
