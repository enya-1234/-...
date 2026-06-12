import streamlit as st
from PIL import Image
from streamlit_js_eval import streamlit_js_eval
import json
from pathlib import Path 

data = streamlit_js_eval(
    js_expressions = f"localStorage.getItem('progress')",
    key = "get_progress"
    )

if data:
    progress = json.loads(data)
else:
    progress = {}

que = st.query_params
site = que.get("site")

if site == "site1":
    
    st.title("물리 - 아이작 뉴턴")
    
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.inven.co.kr/common/image/viewer2.php?file=https%3A%2F%2Fupload2.inven.co.kr%2Fupload%2F2017%2F07%2F02%2Fbbs%2Fi15323579142.png");
    }
   </style>
    """,
    unsafe_allow_html=True
    )
    file_path1 = Path("sciencego.png")
    img = Image.open(file_path1)
    st.image(img)
    

    file_path = Path("ht111.png")
    file_content = file_path.read_bytes()
    expander = st.expander("See explanation")
    expander.write('''
    <아이작 뉴턴>
    
    - 만유인력의 법칙을 제시하여 천체와 지상의 운동을 하나의 원리로 설명했다.
    - 운동의 3법칙을 정립해 고전역학의 기초를 세웠다.
    - 미적분학 발전에 크게 기여하고 광학 연구를 통해 빛의 성질을 밝혀냈다.
    ''')

    if st.download_button(
        label = "Download image",
        data = file_content,
        file_name = "111.png",
        mime = "image/png"
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions = f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                )""",
                key = f"save_site{site}"
            )
        st.success("축하드립니다! 카드를 수집하셨습니다.")
    st.link_button("Linkkkkk]", "https://www.science.org/")
    
if site == "site2":
    st.title("컴퓨터 과학 - 앨런 튜링")

    file_path1 = Path("sciencego.png")
    img = Image.open(file_path1)
    st.image(img)

    file_path = Path("ht222.png")
    file_content = file_path.read_bytes()

    expander = st.expander("See explanation")
    expander.write('''
    <앨런 튜링>
    - 튜링 기계를 고안하여 현대 컴퓨터 과학의 이론적 토대를 마련했다.
    - 제2차 세계대전 중 독일의 에니그마 암호 해독에 핵심적인 역할을 했다.
    - 인공지능의 가능성을 탐구하며 ‘튜링 테스트’를 제안했다.
    ''')

    if st.download_button(
        label = "Download image",
        data = file_content,
        file_name = "222.png",
        mime = "image/png"
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions = f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                )""",
                key = f"save_site{site}"
            )
        st.success("축하드립니다! 카드를 수집하셨습니다.")
    st.link_button("Link", "https://www.science.org/")
    
if site == "site3":
    st.title("생명과학 - 히포크라테스")

    file_path = Path("ht333.png")
    file_content = file_path.read_bytes()

    file_path1 = Path("sciencego.png")
    img = Image.open(file_path1)
    st.image(img)
    
    expander = st.expander("See explanation")
    expander.write('''
    <히포크라테스>
    - 질병을 신의 벌이 아닌 자연적 원인으로 설명하려고 했다.
    - 체계적인 관찰과 기록을 중시하여 의학을 과학적 학문으로 발전시켰다.
    - 의사의 윤리를 강조한 히포크라테스 선서의 전통을 남겼다.
    ''')

    if st.download_button(
        label = "Download image",
        data = file_content,
        file_name = "333.png",
        mime = "image/png"
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions = f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                )""",
                key = f"save_site{site}"
            )
        st.success("축하드립니다! 카드를 수집하셨습니다.")
    st.link_button("Linkkkkk]", "https://www.science.org/")
    
if site == "site4":
    st.title("지구과학 - 알프레드 베게너")

    file_path1 = Path("sciencego.png")
    img = Image.open(file_path1)
    st.image(img)

    file_path = Path("ht555.png")
    file_content = file_path.read_bytes()

    
    expander = st.expander("See explanation")
    expander.write('''
    <알프레드 베게너>
    - 대륙이 이동한다는 대륙이동설을 제안했다.
    - 여러 대륙의 지형과 화석 분포가 유사하다는 증거를 제시했다.
    - 그의 이론은 훗날 판구조론의 발전에 중요한 기반이 되었다.
    ''')

    if st.download_button(
        label = "Download image",
        data = file_content,
        file_name = "555.png",
        mime = "image/png"
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions = f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                )""",
                key = f"save_site{site}"
            )
        st.success("축하드립니다! 카드를 수집하셨습니다.")
    st.link_button("Linkkkkk]", "https://www.science.org/")

if site == "site5":
    st.title("화학 - 마리 퀴리")

    file_path1 = Path("sciencego.png")
    img = Image.open(file_path1)
    st.image(img)
    
    file_path = Path("ht444.png")
    file_content = file_path.read_bytes()

    expander = st.expander("See explanation")
    expander.write('''
    <마리 퀴리>
    - 방사능 연구를 개척하여 새로운 연구 분야를 열었다.
    - 폴로늄과 라듐을 발견해 원자 연구의 발전에 기여했다.
    - 물리학상과 화학상 두 분야에서 노벨상을 수상한 최초의 인물이 되었다
    ''')
    
    if st.download_button(
        label = "Download image",
        data = file_content,
        file_name = "444.png",
        mime = "image/png"
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions = f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                )""",
                key = f"save_site{site}"
            )
        st.success("축하드립니다! 카드를 수집하셨습니다.")
    st.link_button("Linkkkkk]", "https://www.science.org/")
    
count = sum(1 for i in range(5) if progress.get(f"site{i+1}"))
st.write(f" {count} / 5")

page = st.radio(
    "Menu",
    ["Home", "Collection"],
    horizontal = True
    )

if page == "Home":
    st.title("과학자 카드 수집하기...")
    st.write("QR을 스캔해서 5개의 카드를 모으세요...")

if page == "Collection":
    st.title("컬렉션")
    #if count < 5:
     #   st.warning("아직 잠겨있습니다.")
     #   st.stop()
    st.balloons()
    st.success("축하합니다! 모든 카드를 수집하셨습니다")
