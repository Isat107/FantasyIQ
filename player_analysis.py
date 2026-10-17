import pandas as pd

def get_player_summary(df, player_name):

    """Calculate a player's season and recent PPR statistics."""

    player_games = df[

        df["player_display_name"] == player_name

    ].copy()

    if player_games.empty:

        return None

    # Sort games chronologically

    player_games = player_games.sort_values("week")

    # Exclude bye weeks or rows without a game

    player_games = player_games.dropna(

        subset=["fantasy_points_ppr"]

    )

    if player_games.empty:

        return None

    # Total and average fantasy production

    total_points = player_games["fantasy_points_ppr"].sum()

    games_played = len(player_games)

    average_points = total_points / games_played

    # Average fantasy points over the last 3 games

    recent_games = player_games.tail(3)

    last_three_average = (

        recent_games["fantasy_points_ppr"].mean()

    )

    return {

        "name": player_name,

        "position": player_games["position"].iloc[-1],

        "team": player_games["team"].iloc[-1],

        "games": games_played,

        "total_points": round(total_points, 2),

        "average_points": round(average_points, 2),

        "last_three_average": round(

            last_three_average, 2

        ),

        "receptions": player_games["receptions"].sum(),

        "targets": player_games["targets"].sum(),

        "rushing_yards": player_games["rushing_yards"].sum(),

        "receiving_yards": player_games["receiving_yards"].sum(),

    }