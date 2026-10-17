import streamlit as st

# Configure the website

st.set_page_config(

    page_title="FantasyIQ",

    page_icon="🏈",

    layout="wide"

)

# Homepage

st.title("🏈 FantasyIQ")

st.subheader("Your Fantasy Football Analytics Platform")

st.write(

    "Make smarter fantasy football decisions "

    "using NFL statistics and player analysis."

)

st.divider()

# Player comparison section

st.header("Player Comparison")

player1 = st.text_input("Enter Player 1")

player2 = st.text_input("Enter Player 2")

scoring = st.selectbox(

    "Select League Scoring",

    ["PPR", "Half-PPR", "Standard"]

)

if st.button("Compare Players"):

    if player1 and player2:

        st.success(

            f"Comparing {player1} vs {player2} "

            f"using {scoring} scoring!"

        )

    else:

        st.warning("Please enter two players.")