import streamlit as st

st.title("Aránypár Számítás")

# Bekérjük az ismert aránypár első értékeit
szemszam1 = st.number_input("Ismert szemszám:", min_value=0, value=0)
hossz1 = st.number_input("Ismert cm:", min_value=0.0, value=0.0)

# Bekérjük, hogy mit szeretnénk kiszámolni
mit_szamol = st.selectbox("Mit szeretnél kiszámolni?", ("Szem", "cm"))

# A megfelelő érték bekérése
if mit_szamol == "Szem":
    hossz2 = st.number_input("Kívánt cm:", min_value=0.0, value=0.0)
elif mit_szamol == "cm":
    szemszam2 = st.number_input("Kívánt szemszám:", min_value=0, value=0)

# Számol gomb
if st.button("Számol"):
    if mit_szamol == "Szem":
        if hossz1 != 0:
            szemszam2 = (hossz2 * szemszam1) / hossz1
            st.markdown(f"<h2>Kiszámolt szemszám: {szemszam2}</h2>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: smaller;'>Jó kötögetést kívánok!</p>", unsafe_allow_html=True)
        else:
            st.write("Az ismert cm nem lehet nulla.")
    elif mit_szamol == "cm":
        if szemszam1 != 0:
            hossz2 = (szemszam2 * hossz1) / szemszam1
            st.markdown(f"<h2>Kiszámolt hossz: {hossz2} cm</h2>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: smaller;'>Jó kötögetést kívánok!</p>", unsafe_allow_html=True)
        else:
            st.write("Az ismert szemszám nem lehet nulla.")