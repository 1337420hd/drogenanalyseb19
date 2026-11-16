import random
import streamlit as st

# 1. Dataset: German drug name -> (Latin drug name, Latin plant name, family)
DRUGS = {
    "Matricaria recutita": ("Matricariae flos", "Asteraceae", "Kamillenblüten"),
    "Betula pendula": ("Betulae folium", "Betulaceae", "Birkenblätter"),
    "Salvia officinalis": ("Salviae officinalis folium", "Lamiaceae", "Salbeiblätter"),
    "Senna alexandrina": ("Sennae folium", "Fabaceae", "Sennesfliederblättchen"),
    "Arctostaphylos uva-ursi": ("Uvae ursi folium", "Ericaceae", "Bärentraubeblätter"),
    "Urtica dioica": ("Urticae folium", "Urticaceae", "Brennnessel"),
    "Lavandula angustifolia": ("Lavandulae flos", "Lamiaceae", "Lavendelblüten"),
    "Althaea officinalis": ("Althaeae radix", "Malvaceae", "Eibischblätter"),
    "Malva sylvestris": ("Malvae folium", "Malvaceae", "Malvenblätter"),
    "Melissa officinalis": ("Melissae folium", "Lamiaceae", "Melissenblätter"),
    "Mentha x piperita": ("Menthae piperitae folium", "Lamiaceae", "Pfefferminzblätter"),
    "Plantago lanceolata": ("Plantaginis lanceolatae folium", "Plantaginaceae", "Spitzwegerichblätter"),
    "Rubus idaeus": ("Rubi idaei folium", "Rosaceae", "Himbeerblätter"),
    "Arnica montana": ("Arnicae flos", "Asteraceae", "Arnikablüten"),
    "Calendula officinalis": ("Calendulae flos", "Asteraceae", "Ringelblumenblüten"),
    "Hibiscus sabdariffa": ("Hibisci sabdariffae flos", "Malvaceae", "Hibiscusblüten"),
    "Humulus lupulus": ("Lupuli flos", "Cannabaceae", "Hopfenzapfen"),
    "Sambucus nigra": ("Sambuci flos", "Viburnaceae", "Holunderblüten"),
    "Tilia cordata": ("Tiliae flos", "Malvaceae", "Winterlindenblüten"),
    "Verbascum densiflorum": ("Verbasci flos", "Scrophulariaceae", "Königskerzenblüten"),
    "Linum usitatissimum": ("Lini semen", "Linaceae", "Leinsamen"),
    "Pimpinella anisum": ("Anisi fructus", "Apiaceae", "Anis"),
    "Foeniculum vulgare": ("Foeniculi dulcis fructus", "Apiaceae", "Süßer Fenchel"),
    "Juniperus communis": ("Juniperi fructus", "Cupressaceae", "Wacholderbeeren"),
    "Vaccinium myrtillus": ("Myrtilli fructus siccus", "Ericaceae", "getrocknete Heidelbeeren"),
    "Piper nigrum": ("Piperis fructus", "Piperaceae", "Pfeffer"),
    "Rosa canina": ("Rosae pseudo-fructus", "Rosaceae", "Hagebuttenschalen"),
    "Silybum marianum": ("Cardui mariae fructus", "Asteraceae", "Mariendistelfrüchte"),
    "Artemisia absinthium": ("Absinthii herba", "Asteraceae", "Wermutkraut"),
    "Alchemilla vulgaris": ("Alchemillae herba", "Rosaceae", "Frauenmantelkraut"),
    "Crataegus monogyna": ("Crataegi folium cum flore", "Rosaceae", "Weißdornblätter mit Blüten"),
    "Epilobium angustifolium": ("Epilobii angustifolii herba", "Onagraceae", "Weidenröschenkraut"),
    "Equisetum arvense": ("Equiseti herba", "Equisetaceae", "Schachtelhalmkraut"),
    "Hypericum perforatum": ("Hyperici herba", "Hypericaceae", "Johanniskraut"),
    "Achillea millefolium": ("Millefolii herba", "Asteraceae", "Schafgarbenkraut"),
    "Thymus vulgaris": ("Thymi herba", "Lamiaceae", "Thymian"),
    "Viscum album": ("Visci herba", "Santalaceae", "Mistelkraut"),
    "Cinnamomum verum": ("Cinnamomi cortex", "Lauraceae", "Zimtrinde"),
    "Frangula alnus": ("Frangulae cortex", "Rhamnaceae", "Faulbaumrinde"),
    "Quercus robur": ("Quercus cortex", "Fagaceae", "Eichenrinde"),
    "Acorus calamus": ("Calami rhizoma", "Araceae/Acoraceae", "Kalmuswurzelstock"),
    "Zingiber officinale": ("Zingiberis rhizoma", "Zingiberaceae", "Ingwerwurzelstock"),
    "Althaea officinalis": ("Althaeae radix (P)", "Malvaceae", "Eibischwurzel"),
    "Gentiana lutea": ("Gentianae radix", "Gentianaceae", "Enzianwurzel"),
    "Glycyrrhiza glabra": ("Liquiritiae radix", "Fabaceae", "Süßholzwurzel"),
    "Primula veris": ("Primulae radix", "Primulaceae", "Primelwurzel"),
    "Taraxacum officinale": ("Taraxaci officinalis radix", "Asteraceae", "Löwenzahnwurzel"),
    "Valeriana officinalis": ("Valerianae radix", "Valerianaceae", "Baldrianwurzel"),

    

}


def norm(text):
    """Lowercase, trim, collapse spaces, treat the hybrid 'x' loosely."""
    t = " ".join(text.strip().lower().split())
    return t.replace(" x ", " ").replace("×", "")


# 2. Game state
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "current" not in st.session_state:
    st.session_state.current = random.choice(list(DRUGS.keys()))
if "feedback" not in st.session_state:
    st.session_state.feedback = None


def next_question():
    st.session_state.current = random.choice(list(DRUGS.keys()))
    st.session_state.feedback = None


def check_answer(drug_guess, plant_guess, family_guess):
    st.session_state.total_questions += 1
    drug_lat, family, plant_lat = DRUGS[st.session_state.current]

def check_answer(drug_guess, plant_guess, family_guess):
    st.session_state.total_questions += 1
    
    # The key IS the Latin plant name; the 3rd tuple item is the German name
    plant_lat = st.session_state.current
    drug_lat, family, _ = DRUGS[st.session_state.current]
    
    checks = [
        ("🧪 Latin drug name", drug_guess, drug_lat),
        ("🌿 Latin plant name", plant_guess, plant_lat),
        ("🌱 Family", family_guess, family),
    ]
    # ... rest of your function stays the same

    results = [(label, norm(g) == norm(c), c) for label, g, c in checks]

    if all(ok for _, ok, _ in results):
        st.session_state.score += 1
        fb = "✅ All correct!\n\n"
        fb += "\n\n".join(f"{label}: **{c}**" for label, _, c in results)
    else:
        fb = "❌ Not completely correct.\n\n"
        fb += "\n\n".join(
            f"{label}: Correct! (**{c}**)" if ok else f"{label}: **{c}**"
            for label, ok, c in results
        )
    st.session_state.feedback = fb


# 3. UI
st.title("🌿 Drogen-Quiz")
st.write("You see the German drug name. Type the Latin drug name, the Latin plant name and the family.")

st.sidebar.header("🏆 Scoreboard")
st.sidebar.metric("Score", f"{st.session_state.score} / {st.session_state.total_questions}")

st.subheader(f"Drug: **{DRUGS[st.session_state.current][2]}**")

with st.form(key="quiz_form", clear_on_submit=True):
    drug_guess = st.text_input("Latin drug name (e.g. Matricariae flos):")
    plant_guess = st.text_input("Latin plant name (e.g. Matricaria recutita):")
    family_guess = st.text_input("Botanical family:")
    submit = st.form_submit_button("Submit Answer")

    if submit:
        if drug_guess and plant_guess and family_guess:
            check_answer(drug_guess, plant_guess, family_guess)
        else:
            st.warning("Please fill in all three answers!")

if st.session_state.feedback:
    if "✅" in st.session_state.feedback:
        st.success(st.session_state.feedback)
    else:
        st.error(st.session_state.feedback)
    st.button("Next Drug ➡️", on_click=next_question)
