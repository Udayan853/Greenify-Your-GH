import os
import subprocess
import argparse
from datetime import datetime, timedelta

def _validate_date(date:str) -> datetime:
    try:
        timestamp = datetime.strptime(date, "%Y-%m-%d")
        return timestamp
    except ValueError:
        print(f"Error: {date} is not a valid input")
        return None

def main():
    parser = argparse.ArgumentParser(
            prog = "./main.py",
            description = "Fills the user activity graph"
            )
    parser.add_argument("start_date", help = "supply start date in YYYY-MM-DD format, for example 2025-03-03")
    parser.add_argument("end_date", help = "supply end date in YYYY-MM-DD format, for example 2025-04-04")
    parser.add_argument("-f", "--frequency", help = "the number of commits per day, defaults to 1", action = "store_const", default = 1)
    parser.add_argument("-v", "--verbose", action = "store_true")

    args = parser.parse_args()
    start_date = _validate_date(args.start_date)
    end_date = _validate_date(args.end_date)
    commits_per_day = args.frequency
    filename = "sample.py"
    delta = timedelta(days=1)

    if(start_date==None or end_date==None or start_date) >= end_date:
        return
    else:
        d = start_date
        while d <= end_date:
            for i in range(commits_per_day):
                with open(filename, "a") as f:
                    f.write(f"Commit on {d.date()} #{i + 1}\n")

                date_str = d.strftime("%Y-%m-%dT12:00:00")
                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = date_str
                env["GIT_COMMITER_DATE"] = date_str

                subprocess.run(["git", "add", "."])
                subprocess.run(["git","commit","-m","Dummy Commit"], env=env)
            d += delta

if __name__ == "__main__":
    main()
