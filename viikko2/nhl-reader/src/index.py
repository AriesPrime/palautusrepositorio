from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()

    season = Prompt.ask(
        "Season",
        choices=[
            "2018-19",
            "2019-20",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
            "2024-25",
        ],
        default="2024-25",
        console=console,
    )

    nationality = Prompt.ask(
        "Nationality",
        choices=[
            "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR",
            "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB",
            "LAT", "AUS"
        ],
        default="FIN",
        console=console,
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    header = f"Season {season} players from {nationality}"
    table = Table(title=header)

    table.add_column("Released", justify="left")
    table.add_column("teams", justify="left")
    table.add_column("goals", justify="right")
    table.add_column("assists", justify="right")
    table.add_column("points", justify="right")

    for p in players:
        points = p.goals + p.assists
        table.add_row(
            p.name,
            p.team,
            str(p.goals),
            str(p.assists),
            str(points),
        )

    console.print()
    console.print(f"Nationality [{nationality}]")
    console.print(table)


if __name__ == "__main__":
    main()
