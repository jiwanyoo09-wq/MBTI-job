import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="🎯",
    layout="centered"
)

st.title("✨ MBTI 진로 추천기")
st.markdown("### 🎯 나의 MBTI에 어울리는 진로를 알아보자!")
st.write("MBTI를 선택하면 잘 어울리는 진로 2개를 추천해줄게 😎")

# MBTI 데이터
mbti_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석을 좋아하는 사람에게 딱!"
        },
        {
            "career": "🏗️ 건축가",
            "major": "건축학과",
            "personality": "창의적이면서 계획 세우는 걸 좋아하는 사람에게 추천!"
        }
    ],
    "INTP": [
        {
            "career": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 새로운 아이디어를 좋아하는 스타일!"
        },
        {
            "career": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "깊게 탐구하고 혼자 집중하는 걸 잘하는 사람!"
        }
    ],
    "ENTJ": [
        {
            "career": "📈 CEO",
            "major": "경영학과",
            "personality": "리더십 있고 목표를 향해 돌진하는 타입!"
        },
        {
            "career": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적으로 말 잘하고 설득력 있는 사람!"
        }
    ],
    "ENTP": [
        {
            "career": "🎤 마케터",
            "major": "광고홍보학과",
            "personality": "아이디어 많고 사람들과 소통 잘하는 성격!"
        },
        {
            "career": "🚀 스타트업 창업가",
            "major": "경영학과",
            "personality": "도전을 즐기고 새로운 걸 시도하는 걸 좋아함!"
        }
    ],
    "INFJ": [
        {
            "career": "💖 상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 사람 이야기를 잘 들어줌!"
        },
        {
            "career": "✍️ 작가",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 깊은 스타일!"
        }
    ],
    "INFP": [
        {
            "career": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "감성적이고 창의력이 넘치는 사람!"
        },
        {
            "career": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "자신만의 감성을 표현하는 걸 좋아함!"
        }
    ],
    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람들을 이끌고 도와주는 걸 좋아하는 타입!"
        },
        {
            "career": "🎙️ 아나운서",
            "major": "미디어커뮤니케이션학과",
            "personality": "말하는 걸 좋아하고 밝은 에너지가 넘침!"
        }
    ],
    "ENFP": [
        {
            "career": "📹 유튜버",
            "major": "영상학과",
            "personality": "끼 많고 자유로운 분위기를 좋아함!"
        },
        {
            "career": "🌏 여행 콘텐츠 제작자",
            "major": "관광학과",
            "personality": "새로운 경험과 사람 만나는 걸 좋아함!"
        }
    ],
    "ISTJ": [
        {
            "career": "🏦 회계사",
            "major": "세무회계학과",
            "personality": "꼼꼼하고 책임감 강한 사람!"
        },
        {
            "career": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하고 성실함!"
        }
    ],
    "ISFJ": [
        {
            "career": "🩺 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 다른 사람을 잘 챙김!"
        },
        {
            "career": "🏫 사회복지사",
            "major": "사회복지학과",
            "personality": "따뜻하고 책임감 있는 스타일!"
        }
    ],
    "ESTJ": [
        {
            "career": "📊 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십 있는 사람!"
        },
        {
            "career": "🏢 기업 관리자",
            "major": "경영학과",
            "personality": "조직 관리와 계획 세우는 걸 잘함!"
        }
    ],
    "ESFJ": [
        {
            "career": "🧑‍⚕️ 병원 코디네이터",
            "major": "보건행정학과",
            "personality": "친절하고 사람들과 잘 어울림!"
        },
        {
            "career": "🎉 행사 기획자",
            "major": "이벤트학과",
            "personality": "분위기 메이커 역할을 잘함!"
        }
    ],
    "ISTP": [
        {
            "career": "🔧 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 직접 만들고 해결하는 걸 좋아함!"
        },
        {
            "career": "🏍️ 자동차 정비사",
            "major": "자동차학과",
            "personality": "실전 경험과 기술 배우는 걸 즐김!"
        }
    ],
    "ISFP": [
        {
            "career": "📷 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 분위기를 좋아함!"
        },
        {
            "career": "💄 메이크업 아티스트",
            "major": "뷰티학과",
            "personality": "예술 감각이 뛰어나고 섬세함!"
        }
    ],
    "ESTP": [
        {
            "career": "🏀 스포츠 트레이너",
            "major": "체육학과",
            "personality": "활동적이고 에너지가 넘침!"
        },
        {
            "career": "💼 영업 전문가",
            "major": "마케팅학과",
            "personality": "사람들과 금방 친해지고 자신감이 강함!"
        }
    ],
    "ESFP": [
        {
            "career": "🎬 배우",
            "major": "연극영화과",
            "personality": "주목받는 걸 좋아하고 표현력이 풍부함!"
        },
        {
            "career": "🎤 아이돌 트레이너",
            "major": "실용무용과",
            "personality": "밝고 끼가 많은 사람에게 추천!"
        }
    ]
}

# MBTI 선택
selected_mbti = st.selectbox(
    "💡 너의 MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# 버튼
if st.button("🎁 진로 추천 받기"):
    st.success(f"{selected_mbti} 유형에게 어울리는 진로를 소개할게! ✨")

    careers = mbti_data[selected_mbti]

    for idx, item in enumerate(careers, start=1):
        st.markdown(f"## {idx}. {item['career']}")
        st.write(f"🎓 추천 학과 : **{item['major']}**")
        st.write(f"💖 잘 맞는 성격 : {item['personality']}")
        st.markdown("---")

    st.balloons()

st.caption("🌈 재미로 보는 MBTI 진로 추천! 너무 진지하게만 생각하지는 말기 😆")
