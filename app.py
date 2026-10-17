import streamlit as st

from data_loader import load_player_stats

from player_analysis import get_player_summary

st.set_page_config(

    page_title="FantasyIQ",

    page_icon="🏈",

    layout="wide"

)

st.title("🏈 FantasyIQ")

st.subheader("2026 NFL Fantasy Football Analytics")

st.write("Compare real player performances using PPR scoring.")

st.divider()

# Cache data so it isn't downloaded on every interaction

@st.cache_data(ttl=3600)

def get_data():

    return load_player_stats()

df = get_data()

if df.empty:

    st.error("Unable to load NFL statistics.")

    st.stop()

# Create a list of available players

players = sorted(df["player_display_name"].dropna().unique())

st.header("Player Comparison")

col1, col2 = st.columns(2)

with col1:

    player1 = st.selectbox(

        "Select Player 1",

        players,

        index=None,

        placeholder="Choose your first player"

    )

with col2:

    player2 = st.selectbox(

        "Select Player 2",

        players,

        index=None,

        placeholder="Choose your second player"

    )

if st.button("Compare Players"):

    if not player1 or not player2:

        st.warning("Please select two players.")

    elif player1 == player2:

        st.warning("Please select two different players.")

    else:

        stats1 = get_player_summary(df, player1)

        stats2 = get_player_summary(df, player2)

        if stats1 is None or stats2 is None:

            st.error("Could not calculate player statistics.")

        else:

            st.subheader(

                f"{player1} vs. {player2}"

            )

            comparison = {

                "Statistic": [

                    "Position",

                    "Team",

                    "Games Played",

                    "Total PPR Points",

                    "PPR Points Per Game",

                    "Last 3 Games Average",

                    "Receptions",

                    "Targets",

                    "Rushing Yards",

                    "Receiving Yards"

                ],

                player1: [

                    stats1["position"],

                    stats1["team"],

                    stats1["games"],

                    stats1["total_points"],

                    stats1["average_points"],

                    stats1["last_three_average"],

                    stats1["receptions"],

                    stats1["targets"],

                    stats1["rushing_yards"],

                    stats1["receiving_yards"]

                ],

                player2: [

                    stats2["position"],

                    stats2["team"],

                    stats2["games"],

                    stats2["total_points"],

                    stats2["average_points"],

                    stats2["last_three_average"],

                    stats2["receptions"],

                    stats2["targets"],

                    stats2["rushing_yards"],

                    stats2["receiving_yards"]

                ]

            }

            st.dataframe(

                comparison,

                hide_index=True,

                use_container_width=True
            )