import streamlit as st

from functions import f
from streamlit_extras.switch_page_button import switch_page



############################### Variables #####################################

# Initialize variables for Wells' Criteria for PE
	# dct with question: score
	# name for key
wells_pe_dct={
	"Kliniska tecken på DVT": 3,
	"LE mer sannolik än annan diagnos": 3,
	"Hjärtfrekvens >100/min": 1.5,
	"Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1.5,
	"Tidigare LE/DVT diagnos": 1.5,
	"Hemoptys": 1,
	"Malignitet behandlad inom 6 mån eller palliation": 1
	}

wells_pe_name = "wells_pe"

# Initialize variables for PERC Rule for PE
	# dct with question:score
	# name for key

perc_dct={
	"Ålder ≥50": 1,
	"Hjärtfrekvens >100/min": 1,
	"Saturation >94% utan syrgas": 1,
	"Tidigare LE/DVT diagnos": 1,
	"Immobiliserad i >3 dagar / Opererad senaste 4 veckor": 1,
	"Hemoptys": 1,
	"Östrogenbehandling": 1,
	"Kliniska tecken på DVT": 1
}

perc_name = "perc"

######################### Initialize Common variables #########################
# these are all the questions that are common among DVT, PE & PERC

if "immobiliserad eller opererad" not in st.session_state:
    # gemensam för LE, DVT & PERC
    st.session_state["immobiliserad eller opererad"] = False
    # gemensam för LE, DVT & PERC
    st.session_state["tidigare LE eller DVT diagnos"] = False
    # gemensam för LE och DVT
    st.session_state["malignitet eller palliation"] = False
    # gemensam för LE och PERC
    st.session_state["hjärtfrekvens"] = False
    # gemensam för LE och PERC
    st.session_state["Hemoptys"] = False
    # gemensam för LE och PERC
    st.session_state["kliniska tecken DVT"] = False

############################### Initialize PE #################################

f.initialize_keys(wells_pe_dct, wells_pe_name)

if "total_score_pe" not in st.session_state:
	st.session_state["total_score_pe"] = 0

if "pe_done" not in st.session_state:
    st.session_state["pe_done"] = False

if "disabled_pe0" not in st.session_state:
    for i, j in enumerate(wells_pe_dct):
        st.session_state[f"disabled_pe{i}"] = False

############################## Initialize PERC ################################

f.initialize_keys(perc_dct, perc_name)

if "perc_done" not in st.session_state:
    st.session_state["perc_done"] = False
    
if "disabled_perc0" not in st.session_state:
    for i, j in enumerate(perc_dct):
        st.session_state[f"disabled_perc{i}"] = False

################################## Program ####################################
#################################### PE #######################################

st.header("Well's Kriterier för Lungemboli")
st.markdown("---")
f.create_checkboxes_pe(wells_pe_dct, wells_pe_name)
st.markdown("---")

if f.calc_score(perc_dct, perc_name) > 0:
        st.error("PERC bruten")

st.session_state["total_score_pe"] =\
        f.calc_score(wells_pe_dct, wells_pe_name)



f.pe_display(st.session_state["total_score_pe"])


html_låg = 'Om Låg --> <a href="/PERC" target="_self">PERC</a>'
st.markdown(html_låg, unsafe_allow_html=True)

test = st.button("Gå till PERC")
if test:
    switch_page("PERC")

html_låg_perc = 'Om Låg och PERC bruten --> <a href="/Ddimer" target="_self">D-dimer</a>'
st.markdown(html_låg_perc, unsafe_allow_html=True)

html_måttlig = 'Om Måttlig --> <a href="/Ddimer" target="_self">D-dimer</a>'
st.markdown(html_måttlig, unsafe_allow_html=True)

html_hög = 'Om Hög --> <a href="/Röntgen" target="_self">Röntgen</a>'
st.markdown(html_hög, unsafe_allow_html=True)