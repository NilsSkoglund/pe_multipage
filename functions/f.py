### Hej Puran ###
################################# Imports #####################################
import streamlit as st
from PIL import Image

################################ Functions ####################################
def test_func():
    st.write("Haj")
############################# General functions ###############################
    # used for multiple different questionnaries
        # calc_score
        # intialize_keys
def calc_score(dct, name):
	'''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	calculates total score for:
        DVT
        PE
        PERC
        PESI
	'''
	total_score = 0
	for index, question in enumerate(dct):
		key = f"{name}{index}"
		if st.session_state[key]: # if True means the checkbox is ticked
			total_score += dct.get(question)
	return total_score

def initialize_keys(dct, name):
	'''
    Takes a dictionary (dvt) and a string (name) as inputs and ...
	initializes session state 'keys' for:
        DVT
        PE
        PERC
        PESI
    
    Note! More session state 'keys' are initialized ...
    at other places for other purposes for DVT, PE, PERC & PESI
	'''
	for index, j in enumerate(dct):
		key = f"{name}{index}"
		if key not in st.session_state:
			st.session_state[key] = False
	return None

######################## General functions - THE END ##########################

############################### Functions DVT #################################
    # function(s) only used for the DVT questionnaire
        # create_checkboxes_dvt
        # sync answers functions (3 similar functions)
        # change_dvt_in_to_out

def create_checkboxes_dvt(dct, name):
    '''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	creates checkboxes for the different questions:
    '''
    for index, question in enumerate(dct.items()):
        if question[0] not in wells_pe_dct:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                disabled = st.session_state[f"disabled_dvt{index}"]
            )
        elif index==6:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                value=st.session_state["immobiliserad eller opererad"],
                on_change=sync_from_dvt6_to_pe3_and_perc4,
                disabled = st.session_state["disabled_dvt6"]
			)
        elif index==7:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                value=st.session_state["malignitet eller palliation"],
                on_change=sync_from_dvt7_to_pe6,
                disabled = st.session_state["disabled_dvt7"]
            )
        elif index==8:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                value=st.session_state["tidigare LE eller DVT diagnos"],
                on_change=sync_from_dvt8_to_pe4_and_perc3,
                disabled = st.session_state["disabled_dvt8"]
            )

# sync answers from DVT questionnarie to PE & PERC questionnaries
    # immobiliserad eller opererad (PE & PERC)
    # malignitet eller palliation (only PE)
    # tidigare LE eller DVT diagnos (PE & PERC)

def sync_from_dvt6_to_pe3_and_perc4():
    '''
    index DVT dict: 6
    index PE dict: 3
    index PERC dict: 4
    '''
    st.session_state["immobiliserad eller opererad"]=\
		st.session_state["wells_dvt6"]

def sync_from_dvt7_to_pe6():
    '''
    index DVT dict: 7
    index PE dict: 6
    '''
    st.session_state["malignitet eller palliation"]=\
		st.session_state["wells_dvt7"]

def sync_from_dvt8_to_pe4_and_perc3():
    '''
    index DVT dict: 8
    index PE dict: 4
    index PERC dict: 3
    '''
    st.session_state["tidigare LE eller DVT diagnos"]=\
		st.session_state["wells_dvt8"]

# sync "done" checkbox and disable checkboxes in questionnarie
def change_dvt_in_to_out():
    '''
    when "done" checkbox is marked within a questionnarie ...
    update the checkboxes in the "öppna/stäng överblick" expander ...
    and disable checkboxes with questions (inside of questionnarie).
    '''
    st.session_state["dvt_done"] = st.session_state["dvt_mark_inside"]
    for i, j in enumerate(wells_dvt_dct):
        st.session_state[f"disabled_dvt{i}"] = st.session_state["dvt_done"]

########################### Functions DVT - THE END ###########################

################################# Functions PE ################################
    # function(s) only used for the PE questionnaire
        # create_checkboxes_pe
        # sync answers functions (6 similar functions)
        # change_pe_in_to_out
        # pe_display
        # pe_algo

def create_checkboxes_pe(dct, name):
    '''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	creates checkboxes for the different questions:
    '''
    for index, question in enumerate(dct.items()):
        if index == 0:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                on_change=sync_from_pe0_to_perc7,
                value=st.session_state["kliniska tecken DVT"],
                disabled = st.session_state["disabled_pe0"]
            )
        elif index == 2:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                on_change=sync_from_pe2_to_perc1,
                value=st.session_state["hjärtfrekvens"],
                disabled = st.session_state["disabled_pe2"]
            )

        elif index==3:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                on_change=sync_from_pe3_to_perc1_and_dvt6,
                value=st.session_state["immobiliserad eller opererad"],
                disabled = st.session_state["disabled_pe3"]
            )
        elif index==4:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                on_change=sync_from_pe4_to_perc3_and_dvt8,
                value=st.session_state["tidigare LE eller DVT diagnos"],
                disabled = st.session_state["disabled_pe4"]
            )
        elif index ==5:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                on_change=sync_from_pe5_to_perc5,
                value=st.session_state["Hemoptys"],
                disabled = st.session_state["disabled_pe5"]
            )
        elif index==6:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                on_change=sync_from_pe6_to_dvt7,
                value=st.session_state["malignitet eller palliation"],
                disabled = st.session_state["disabled_pe6"]
            )
        else:
            st.checkbox(
                label=f"{question[0]} ({question[1]}p)",
                key=f"{name}{index}",
                disabled = st.session_state[f"disabled_pe{index}"]
            )

# sync answers from PE questionnarie to DVT & PERC questionnaries
    # kliniska tecken DVT (only PERC)
    # hjärtfrekvens (only PERC)
    # immobiliserad eller opererad (PERC & DVT)
    # tidigare LE eller DVT diagnos (PERC & DVT)
    # Hemoptys (only PERC)
    # malignitet eller palliation (only DVT)

def sync_from_pe0_to_perc7():
    st.session_state["kliniska tecken DVT"] =\
        st.session_state["wells_pe0"]

def sync_from_pe2_to_perc1():
    st.session_state["hjärtfrekvens"] =\
        st.session_state["wells_pe2"]

def sync_from_pe3_to_perc1_and_dvt6():
    st.session_state["immobiliserad eller opererad"] =\
        st.session_state["wells_pe3"]

def sync_from_pe4_to_perc3_and_dvt8():
    st.session_state["tidigare LE eller DVT diagnos"] =\
        st.session_state["wells_pe4"]

def sync_from_pe5_to_perc5():
    st.session_state["Hemoptys"] =\
        st.session_state["wells_pe5"]

def sync_from_pe6_to_dvt7():
    st.session_state["malignitet eller palliation"] =\
        st.session_state["wells_pe6"]

def change_pe_in_to_out():
    '''
    when "done" checkbox is marked within a questionnarie ...
    update the checkboxes in the "öppna/stäng överblick" expander ...
    and disable checkboxes with questions (inside of questionnarie).
    For the PE questionnarie we also loop through PERC and disable the ...
    checkboxes with questions present in the the PE questionnarie
    '''
    st.session_state["pe_done"] = st.session_state["pe_mark_inside"]
    for i, j in enumerate(wells_pe_dct):
        st.session_state[f"disabled_pe{i}"] = st.session_state["pe_done"]

    index_perc_in_pe = [1,3,4,5,7] # index for questions in PERC present in PE
    for i in index_perc_in_pe:
        st.session_state[f"disabled_perc{i}"] = st.session_state["pe_done"]

def pe_display(total_score):
	'''
    Takes a float as input and ...
	displays result image for PE. One of 24 different images based on score
	'''
	text_total_score = str(int(total_score*10))
	image = Image.open(f"img/t{text_total_score}.png")
	return st.image(image)

def pe_algo():
    '''
    write a docstring!
    '''
    score_pe = st.session_state["total_score_pe"]
    score_perc = calc_score(perc_dct, perc_name)
    if score_pe < 1.5 and score_perc == 0:
        st.info("Låg risk & PERC ej bruten. Gå vidare till PERC")
    elif score_pe < 1.5 and score_perc > 0:
        st.info("Låg risk men PERC bruten. Gå vidare till D-dimer")
    elif 1.5 < score_pe < 6.5:
        st.info("Måttlig risk. Gå vidare till D-dimer")
    else:
        st.info("Hög risk. Gå vidare till Röntgen")

############################ Functions PE - THE END ###########################

################################ Functions PERC ###############################
    # function(s) only used for the PERC questionnaire
        # create_checkboxes_perc
        # sync answers functions (5 similar functions)
        # change_perc_in_to_out
def create_checkboxes_perc(dct, name):
    '''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	creates checkboxes for the different questions:
    '''
    for index, question in enumerate(dct.items()):
        if index == 1:
            st.checkbox(
                label=f"{question[0]}",
                key=f"{name}{index}",
                on_change=sync_from_perc1_to_pe2,
                value=st.session_state["hjärtfrekvens"],
                disabled = st.session_state[f"disabled_perc{index}"]
            )
        elif index == 3:
            st.checkbox(
                label=f"{question[0]}",
                key=f"{name}{index}",
                on_change=sync_from_perc3_to_pe4_and_dvt8,
                value=st.session_state["tidigare LE eller DVT diagnos"],
                disabled = st.session_state[f"disabled_perc{index}"]
            )
        elif index == 4:
            st.checkbox(
                label=f"{question[0]}",
                key=f"{name}{index}",
                on_change=sync_from_perc4_to_pe3_and_dvt6,
                value=st.session_state["immobiliserad eller opererad"],
                disabled = st.session_state[f"disabled_perc{index}"]
            )
        elif index == 5:
            st.checkbox(
                label=f"{question[0]}",
                key=f"{name}{index}",
                on_change=sync_from_perc5_to_pe5,
                value=st.session_state["Hemoptys"],
                disabled = st.session_state[f"disabled_perc{index}"]
            )
        elif index == 7:
            st.checkbox(
                label=f"{question[0]}",
                key=f"{name}{index}",
                on_change=sync_from_perc7_to_pe0,
                value=st.session_state["kliniska tecken DVT"],
                disabled = st.session_state[f"disabled_perc{index}"]
            )
        else:
            st.checkbox(
                label=f"{question[0]}",
                key=f"{name}{index}",
                disabled = st.session_state[f"disabled_perc{index}"]
            )

# sync answers from PERC questionnarie to PE & DVT questionnaries
    # hjärtfrekvens (only PE)
    # tidigare LE eller DVT diagnos (PE & DVT)
    # immobiliserad eller opererad (PE & DVT)
    # Hemoptys (only PE)
    # kliniska tecken DVT (only PE)

def sync_from_perc1_to_pe2():
    st.session_state["hjärtfrekvens"] =\
        st.session_state["perc1"]

def sync_from_perc3_to_pe4_and_dvt8():
    st.session_state["tidigare LE eller DVT diagnos"] =\
        st.session_state["perc3"]

def sync_from_perc4_to_pe3_and_dvt6():
    st.session_state["immobiliserad eller opererad"] =\
        st.session_state["perc4"]

def sync_from_perc5_to_pe5():
    st.session_state["Hemoptys"] =\
        st.session_state["perc5"]

def sync_from_perc7_to_pe0():
    st.session_state["kliniska tecken DVT"] =\
        st.session_state["perc7"]

def change_perc_in_to_out():
    '''
    when "done" checkbox is marked within a questionnarie ...
    update the checkboxes in the "öppna/stäng överblick" expander ...
    and disable checkboxes with questions (inside of questionnarie)
    '''
    st.session_state["perc_done"] = st.session_state["perc_mark_inside"]
    for i, j in enumerate(perc_dct):
        st.session_state[f"disabled_perc{i}"] = st.session_state["perc_done"]

########################### Functions PERC - THE END ##########################

############################## Functions D-dimer ##############################
    # function(s) only used for the D-dimer questionnaire/expander
def Ddimer_beslutsgräns():
    '''
    Funtions that returns the threshold value for D-dimer 
    '''
    if st.session_state["Ddimer_age"] <= 50:
        return 0.50
    else:
        return st.session_state["Ddimer_age"]/100

def Ddimer_display():
    '''
    display function for D-dimer. Checks if score is above/below threshold ...
    and displays result/recommendations accordingly
    '''
    if st.session_state["Ddimer_result"] > Ddimer_beslutsgräns():
        st.write(f"Ålderbaserad beslutsgräns: >{Ddimer_beslutsgräns()}")
        st.write(f"Resultat: {round(st.session_state['Ddimer_result'],2)}")
        st.info(f"Positivt D-dimer test. Gå vidare till röntgen")
    else:
        st.write(f"Ålderbaserad beslutsgräns: >{Ddimer_beslutsgräns()}")
        st.write(f"Resultat: {round(st.session_state['Ddimer_result'],2)}")
        st.info(f"Negativt D-dimer test")

def change_ddimer_in_to_out():
    '''
    when "done" checkbox is marked within a questionnarie ...
    update the checkboxes in the "öppna/stäng överblick" expander ...
    and disable checkboxes with questions (inside of questionnarie)
    '''
    st.session_state["ddimer_done"] =\
        st.session_state["ddimer_mark_inside"]

    for i in range(2):
        st.session_state[f"disabled_ddimer{i}"] =\
            st.session_state["ddimer_done"]

######################### Functions D-dimer - THE END #########################

############################### Functions PESI ################################
    # function(s) only used for the PESI questionnaire

def create_checkboxes_pesi(dct, name):
    '''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	creates checkboxes for the different questions:
    '''
    for index, question in enumerate(dct.items()):
        st.checkbox(
            label=f"{question[0]} ({question[1]}p)",
            key=f"{name}{index}"
        )