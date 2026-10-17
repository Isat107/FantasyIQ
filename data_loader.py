import pandas as pd

SEASON = 2026

DATA_URL = (
"https://github.com/nflverse/nflverse-data/"
"releases/download/stats_player/"
f"stats_player_week_{SEASON}.csv"
)


def load_player_stats():
    """Download weekly NFL player statistics."""
    try:
        df = pd.read_csv(DATA_URL)

        # Keep regular-season games only
        df = df[df["season_type"] == "REG"]

        # Keep only fantasy offensive players
        fantasy_positions = ["QB", "RB", "WR", "TE"]
        df = df[df["position"].isin(fantasy_positions)]

        # Select statistics useful for fantasy football
        columns = [
            "player_id",
            "player_display_name",
            "position",
            "team",
            "week",
            "opponent_team",
            "fantasy_points_ppr",
            "passing_yards",
            "passing_tds",
            "rushing_yards",
            "rushing_tds",
            "receptions",
            "targets",
            "receiving_yards",
            "receiving_tds",
        ]
        
        df = df[columns].copy()
        
        return df

    except Exception as error:
        print(f"Error loading NFL data: {error}")
        return pd.DataFrame()


if __name__ == "__main__":
    stats = load_player_stats()

    if not stats.empty:
        print("NFL data loaded successfully!")
        print(f"Total player-game records: {len(stats)}")
        print(stats.head())
    else:
        print("No player statistics were loaded.")