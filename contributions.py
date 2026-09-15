import os
import subprocess
from datetime import date, timedelta

start = date(2025, 5, 1)
end = date.today()

current = start

while current <= end:
    # Monday-Friday
    if current.weekday() < 5:
        filename = "activity.txt"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Activity: {current}\n")

        timestamp = f"{current}T12:00:00+0530"

        subprocess.run(
            ["git", "add", filename],
            check=True
        )

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = timestamp
        env["GIT_COMMITTER_DATE"] = timestamp

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                f"chore: activity {current}",
            ],
            env=env,
            check=True
        )

    current += timedelta(days=1)

print(f"Done! Generated activity from {start} to {end}.")