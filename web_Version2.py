import streamlit as st
import yt_dlp
import requests

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Bloodmoon Anime",
    page_icon=":tada:",
    layout="wide",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: #0d0d12;
        color: #f5f5f5;
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background: linear-gradient(180deg, #0d0d12 0%, #14181f 100%);
    }

    .hero {
        background: linear-gradient(135deg, rgba(255,79,79,0.18), rgba(70,80,120,0.15));
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 22px;
        padding: 2rem 2rem;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #ff5c5c;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }

    .subtext {
        color: #d7d9df;
        font-size: 1rem;
    }

    .anime-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem;
        height: 100%;
    }

    .anime-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 0.8rem;
        margin-bottom: 0.3rem;
    }

    .small-label {
        color: #ff7b7b;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        font-size: 0.75rem;
    }

    div[data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.03);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
        padding: 0.3rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #ff5c5c, #ff7d5c);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.7rem 1.5rem;
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.02);
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
    }

    a {
        color: #ff8a8a;
        text-decoration: none;
    }

    a:hover {
        color: #ffd1d1;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helper functions
# -----------------------------
def search_youtube(query: str, max_result: int = 10):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": False,
    }
    search_query = f"ytsearch{max_result}:{query}"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(search_query, download=False)
        return result.get("entries", []) if result else []

# -----------------------------
# Header / Hero
# -----------------------------
with st.container():
    st.markdown(
        """
        <div class="hero">
            <div class="small-label">Welcome</div>
            <h1 style="font-size:3rem; font-weight:800; margin:0.2rem 0 0.5rem 0;">BLOODMOON</h1>
            <p class="subtext" style="font-size:1.1rem;">
                Your anime and manga world — discover series, watch trailers, upload your own videos, and explore more.
            </p>
            <p class="subtext">
                <a href="https://animepahe.pw" target="_blank">Watch anime →</a>
                &nbsp; | &nbsp;
                <a href="https://mangaplus.shueisha.co.jp/" target="_blank">Read manga →</a>
                &nbsp; | &nbsp;
                <a href="https://www.meta.ai/share/a/18171edd-e894-4cbc-8992-89305162d1f8" target="_blank">Read this self-made manga →</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# About section
# -----------------------------
with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown('<div class="section-title">What we plan to achieve</div>', unsafe_allow_html=True)
        st.write(
            """
            We want to build a place where anime lovers can discover trending titles,
            watch videos, and easily explore their favorite series in one friendly interface.
            """
        )
        st.markdown("[Explore anime >](https://animepahe.pw)", unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="section-title">Why this website?</div>', unsafe_allow_html=True)
        st.write(
            """
            This project is a simple anime-themed demo website created for fun and learning.
            It includes anime highlights, manga access, search features, and a clean viewing experience.
            """
        )


# -----------------------------
# Manga section
# -----------------------------
st.markdown('<div class="section-title">Manga</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="anime-card">
        <div class="anime-title">Read manga online</div>
        <p>Explore popular manga titles and continue your favorite stories with a manga platform.</p>
        <a href="https://mangaplus.shueisha.co.jp/" target="_blank">Open MangaPlus →</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Watch videos
# -----------------------------
with st.container():
    uploaded_video = st.file_uploader("Choose a video to upload....", type=["mov","mp4","mkv"])
    if uploaded_video is not None:
        st.video(uploaded_video)
        st.success(f"video uploaded: {uploaded_video.name}")
        st.write(f"File size: {uploaded_video.size / (1024*1024):2f} MB")
    else:
        st.info("please upload a video file")
    # Function to search youTube
    def search_youtube(query,max_result=10):
        ydl_opts={
            'quiet': True,
            'skip_download': True,
            'extract_flat': False,
        }
        search_query=f"ytsearch{max_result}:{query}"
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result=ydl.extract_info(search_query, download=False)
            return result.get('entries',[])

    # Input box
    user_input=st.text_input(
        "Paste any video URL or type what you want to search (e.g. 'demon slayer', 'jujutsu kaisen')",
        placeholder="Type here..."
        )

    if user_input:
        # Check if it's a URL
        is_url = user_input.startswith("http") or "youtube.com" in user_input or "youtu.be" in user_input or "tiktok.com" in user_input

        if is_url:
            st.subheader("🎬 Playing from URL")
            # Streamlit can play youtube,MP4 links, MOV,MKV,VID links directly
            st.video(user_input)
        else:
            st.subheader(f"🔍 Searching internet for: {user_input}")
            with st.spinner("Searching..."):
                try:
                    videos = search_youtube(user_input,24)
                    if videos:
                        cols=st.columns(4)
                        for i, video in enumerate(videos):
                            if video:
                                with cols[i % 3]:
                                    st.video(video.get('webpage_url'))
                                    st.write(f"**{video.get('title')}**")
                                    st.caption(f"Channel: {video.get('Channel')}")
                    else:
                        st.warning("No videos found. try another search.")
                except Exception as e:
                    st.error(f"Error:{e}")
                    st.info("Try pasting a direct youtube link instead.")
    st.write("Works with: youtube links,Tiktok links or just text search")
    st.divider()

# -----------------------------
# Header / Hero
# -----------------------------
with st.container():
    st.markdown(
        """
        <div class="hero">
            <p class="subtext">
                <a href="http://127.0.0.1:8502" target="_blank">Contact Me →</a>
                &nbsp; | &nbsp;
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
