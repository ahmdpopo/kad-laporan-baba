import base64
from pathlib import Path
import time
import streamlit as st

# ==========================================
# 🎯 UBAH SUAI PANTAS (Edit bahagian ini!)
# ==========================================
CONFIG = {
    "dad_name": "Baba",
    "turning_age": 53,  # Tukar ikut umur Baba
    "your_name": "Afif",
    "signature_habit_1": "Semua benda yang baba nak usahakan mesti akan dapat walaupun mula dari kosong.",
    "signature_habit_2": "The most best supportive dad in the world, sentiasa ada bila kami perlukan baba",
    "personal_note": (
        "Selamat Hari Jadi, Baba! Afif minta maaf sangat-sangat sebab tak dapat nak buat banyak untuk birthday baba kalini"
        " sebab Afif tengah busy dengan kelas, projek, dan "
        "macam-macam urusan dekat uni, tapi macam mana pun, Afif tak pernah lupa hari baba yang special ni. "
        "dan segala pengorbanan Baba untuk kami semua. Terima kasih sebab sentiasa support Afif dalam apa jua pun, "
        "bagi nasihat, dan jadi contoh terbaik untuk Afif. Semoga Baba sentiasa sihat,panjang umur, handsome selalu "
        "diperbanyakkan rezeki, dan berjaya dunia akhirat!"
        " Sebab baba dah banyak berusaha untuk mencapai kejayaan dalam hidup."
        " Baba sampai dah bukak branch baru dekat kajang itu memang Afif proud dengan bapak saya ni."
        "I love you so much Baba. Nanti Afif balik KL kita celebrate lebih lagi."
    ),
    "logo_file": "Royal_Enfield_logo_PNG_(8).png",
}


def get_base64_image(image_name: str) -> str:
    """Cari gambar di folder sama dengan app.py (atau mana-mana fail Royal Enfield PNG/JPG)."""
    app_dir = Path(__file__).resolve().parent
    candidate = app_dir / image_name

    # Jika nama fail tepat tak jumpa, cari mana-mana fail .png/.jpg dalam folder yang sama
    if not candidate.exists():
        for f in app_dir.iterdir():
            if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                candidate = f
                break

    if candidate.exists() and candidate.is_file():
        ext = candidate.suffix.lower().lstrip(".") or "png"
        if ext == "jpg":
            ext = "jpeg"
        encoded = base64.b64encode(candidate.read_bytes()).decode("utf-8")
        return f"data:image/{ext};base64,{encoded}"
    return ""


# ==========================================
# 🏍️ ROYAL ENFIELD HERITAGE UI STYLING
# ==========================================
st.set_page_config(
    page_title=f"Kad Laporan Baba v{CONFIG['turning_age']}.0",
    page_icon="🏍️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background-color: #f4efe6;
    background-image: radial-gradient(#d6cbb8 1px, transparent 1px);
    background-size: 20px 20px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #1c1917;
}

.block-container {
    padding-top: 1.1rem !important;
    padding-bottom: 2.5rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 480px !important;
}

h1, h2, h3, h4 {
    font-family: 'Cinzel', serif !important;
    letter-spacing: 0.02em;
}

.pinstripe-bar {
    height: 6px;
    background: linear-gradient(90deg, #143628 0%, #d4af37 35%, #dc2626 50%, #d4af37 65%, #143628 100%);
    border-radius: 999px;
    margin-bottom: 12px;
}

.mobile-hero {
    background: linear-gradient(145deg, #0f291e 0%, #1b4332 60%, #143628 100%);
    border: 3px solid #d4af37;
    border-radius: 22px;
    padding: 20px 18px;
    color: #fefce8;
    margin-bottom: 16px;
    box-shadow: 0 12px 26px -6px rgba(15, 41, 30, 0.45);
}

.re-logo-banner {
    background: rgba(255, 255, 255, 0.96);
    border: 2px solid #d4af37;
    border-radius: 14px;
    padding: 10px 16px;
    margin-bottom: 14px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}

.re-logo-banner img {
    max-height: 54px;
    width: auto;
    max-width: 100%;
    object-fit: contain;
    display: inline-block;
}

.status-pill {
    display: inline-block;
    background: linear-gradient(135deg, #f59e0b 0%, #d4af37 100%);
    color: #1c1917;
    font-size: 0.7rem;
    font-weight: 900;
    padding: 4px 12px;
    border-radius: 999px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    box-shadow: 0 2px 8px rgba(212, 175, 55, 0.4);
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 9px;
    margin-bottom: 18px;
}

.kpi-card {
    background: #1c1917;
    border: 2.5px solid #d4af37;
    border-radius: 18px;
    padding: 12px 6px;
    text-align: center;
    color: #fafaf9;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.18);
}

.kpi-label {
    font-size: 0.65rem;
    color: #d6d3d1;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.kpi-value {
    font-family: 'Cinzel', serif;
    font-size: 1.25rem;
    font-weight: 800;
    color: #fbbf24;
    margin: 3px 0;
}

.kpi-sub {
    font-size: 0.66rem;
    color: #34d399;
    font-weight: 700;
}

.subject-card {
    background: #ffffff;
    border: 1.5px solid #d6cbb8;
    border-left: 6px solid #1b4332;
    border-radius: 16px;
    padding: 14px 16px;
    margin-bottom: 11px;
    box-shadow: 0 4px 12px rgba(28, 25, 23, 0.06);
}

.subject-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
}

.subject-title {
    font-weight: 800;
    font-size: 0.92rem;
    color: #1c1917;
}

.grade-badge {
    background: #fef3c7;
    color: #92400e;
    border: 1.5px solid #d4af37;
    font-weight: 800;
    font-size: 0.78rem;
    padding: 2px 10px;
    border-radius: 999px;
}

.bar-bg {
    background: #e7e5e4;
    border-radius: 999px;
    height: 9px;
    width: 100%;
    overflow: hidden;
    margin-bottom: 6px;
}

.bar-fill {
    background: linear-gradient(90deg, #1b4332, #d4af37, #dc2626);
    height: 100%;
    border-radius: 999px;
}

.subject-note {
    font-size: 0.82rem;
    color: #44403c;
    line-height: 1.38;
}

.trait-box {
    background: #fffbeb;
    border: 1.5px solid #d4af37;
    border-left: 6px solid #b45309;
    border-radius: 14px;
    padding: 12px 14px;
    margin-bottom: 10px;
    font-size: 0.88rem;
    color: #1c1917;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.04);
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #1b4332 0%, #0f291e 100%) !important;
    color: #fbbf24 !important;
    border: 2.5px solid #d4af37 !important;
    border-radius: 18px !important;
    padding: 0.95rem 1rem !important;
    font-family: 'Cinzel', serif !important;
    font-size: 1.02rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.03em !important;
    box-shadow: 0 10px 22px -4px rgba(15, 41, 30, 0.45) !important;
}

.message-card {
    background: #ffffff;
    border: 3px solid #d4af37;
    border-radius: 20px;
    padding: 20px;
    color: #1c1917;
    line-height: 1.65;
    font-size: 0.96rem;
    box-shadow: 0 10px 25px rgba(28, 25, 23, 0.12);
}

.re-card-crest {
    text-align: center;
    margin-bottom: 10px;
}

.re-card-crest img {
    max-height: 36px;
    width: auto;
    object-fit: contain;
}

.re-footer-strip {
    margin-top: 14px;
    padding-top: 10px;
    border-top: 1.5px dashed #d4af37;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.8rem;
    font-weight: 800;
    color: #1b4332;
}
</style>""",
    unsafe_allow_html=True,
)

# ==========================================
# 🧾 HEADER UTAMA
# ==========================================
st.markdown('<div class="pinstripe-bar"></div>', unsafe_allow_html=True)

logo_uri = get_base64_image(CONFIG["logo_file"])
hero_logo_html = (
    f'<div class="re-logo-banner"><img src="{logo_uri}" alt="Royal Enfield" /></div>'
    if logo_uri
    else ""
)
card_logo_html = (
    f'<div class="re-card-crest"><img src="{logo_uri}" alt="Royal Enfield" /></div>'
    if logo_uri
    else ""
)

st.markdown(
    f"""<div class="mobile-hero">
{hero_logo_html}
<span class="status-pill">🏍️ Penilaian Tahunan Rasmi • Lulus Cemerlang</span>
<h2 style="margin: 10px 0 4px 0; font-size: 1.55rem; line-height: 1.25; color: #fbbf24;">
Kad Laporan {CONFIG['dad_name']}<br/>Edisi Hari Jadi Ke-{CONFIG['turning_age']} 🎂
</h2>
<p style="margin: 6px 0 0 0; color: #e7e5e4; font-size: 0.86rem;">
Penerima: <strong>{CONFIG['dad_name']}</strong> &nbsp;•&nbsp;
Disemak oleh: <strong>{CONFIG['your_name']}</strong>
</p>
</div>""",
    unsafe_allow_html=True,
)

# ==========================================
# 📊 3 KAD KPI UTAMA
# ==========================================
st.markdown(
    """<div class="kpi-grid">
<div class="kpi-card">
<div class="kpi-label">Gred Penuh</div>
<div class="kpi-value">A++</div>
<div class="kpi-sub">Terbaik Dunia</div>
</div>
<div class="kpi-card">
<div class="kpi-label">Nasihat</div>
<div class="kpi-value">99.9%</div>
<div class="kpi-sub">Sentiasa Tepat</div>
</div>
<div class="kpi-card">
<div class="kpi-label">Sokongan</div>
<div class="kpi-value">24/7</div>
<div class="kpi-sub">Tak Pernah Gagal</div>
</div>
</div>""",
    unsafe_allow_html=True,
)

# ==========================================
# 📋 SENARAI MARKAH SUBJEK
# ==========================================
st.markdown("#### 📋 Keputusan Subjek Utama")

subjects = [
    (
        "1. Nasihat & Panduan Hidup",
        "A+",
        100,
        "Sentiasa tepat pada masanya, dan sangat berguna dalam journey hidup Afif.",
    ),
    (
        "2. Sentiasa Ada Di Belakang Afif",
        "100%",
        100,
        "Tak pernah berkira masa dan tenaga bila anak perlukan bantuan.",
    ),
    (
        "3. Kemahiran Repair & DIY",
        "A",
        96,
        "Baba mesti boleh repair ah walau macam mana pun. dari sebatang kayu pun boleh jadi something. hehe",
    ),
    (
        "4. Talent dan Kemahiran",
        "A+",
        100,
        "Lawak baba memang on top, always a champion in our hearts.",
    ),
]

for title, grade, pct, note in subjects:
    st.markdown(
        f"""<div class="subject-card">
<div class="subject-top">
<span class="subject-title">{title}</span>
<span class="grade-badge">{grade}</span>
</div>
<div class="bar-bg">
<div class="bar-fill" style="width: {pct}%;"></div>
</div>
<div class="subject-note">{note}</div>
</div>""",
        unsafe_allow_html=True,
    )

st.markdown("#### ⭐ Kuasa Super Baba")
st.markdown(
    f"""<div class="trait-box">💪 <strong>Kelebihan #1:</strong> {CONFIG['signature_habit_1']}</div>
<div class="trait-box">🧠 <strong>Kelebihan #2:</strong> {CONFIG['signature_habit_2']}</div>""",
    unsafe_allow_html=True,
)

st.write("")

# ==========================================
# 🎁 BUTANG BUKA KAD UCAPAN
# ==========================================
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.markdown("#### 🎁 Tekan Sini Untuk Surprise Baba")
    st.caption("Tekan butang hijau di bawah untuk buka kad ucapan hari lahir Baba.")
    if st.button("🏍️ Tekan Untuk Buka Kad Hari Lahir"):
        with st.status("Mengesahkan status Baba terbaik...", expanded=False) as status:
            time.sleep(0.6)
            status.update(label="Sah! Selamat Hari Jadi Bapak saya yang hebat ni!", state="complete")
        st.session_state.unlocked = True
        st.balloons()
        st.rerun()
else:
    st.markdown(
        f"""<div class="message-card">
{card_logo_html}
<h3 style="margin-top:0; color:#1b4332;">🎉 Selamat Hari Jadi Bapak saya yang hebat ni!</h3>
<p style="margin-bottom:0;">{CONFIG['personal_note']}</p>
<div class="re-footer-strip">
<span>🏍️ MADE LIKE A GUN</span>
<span>— Daripada Anak Kesayangan Baba ❤️</span>
</div>
</div>""",
        unsafe_allow_html=True,
    )