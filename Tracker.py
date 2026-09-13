import csv
from datetime import datetime, timedelta
from pathlib import Path

FILE = Path("job_applications.csv")
WEEKLY_GOAL = 50


def setup_file():
    if not FILE.exists():
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "date",
                "company",
                "position",
                "status"
            ])


def add_application():
    company = input("Company: ")
    position = input("Position: ")
    status = input("Status (Applied/Interview/Rejected/etc.): ") or "Applied"

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            date,
            company,
            position,
            status
        ])

    print("\nApplication added successfully!")


def get_applications():
    with open(FILE, "r", newline="") as file:
        return list(csv.DictReader(file))


def show_progress():
    applications = get_applications()

    today = datetime.now().date()

    # Monday = start of week
    start_of_week = today - timedelta(days=today.weekday())

    today_count = 0
    week_count = 0

    for app in applications:
        app_date = datetime.strptime(
            app["date"], "%Y-%m-%d"
        ).date()

        if app_date == today:
            today_count += 1

        if start_of_week <= app_date <= today:
            week_count += 1

    remaining = max(WEEKLY_GOAL - week_count, 0)

    print("\n==============================")
    print("       JOB APPLICATIONS")
    print("==============================")
    print(f"Today:              {today_count}")
    print(f"This week:          {week_count}/{WEEKLY_GOAL}")
    print(f"Remaining:          {remaining}")

    progress = int((week_count / WEEKLY_GOAL) * 20)
    progress = min(progress, 20)

    bar = "█" * progress + "░" * (20 - progress)

    print(f"\nProgress: [{bar}]")
    print("==============================\n")


def main():
    setup_file()

    while True:
        print("1. Add application")
        print("2. Show progress")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_application()

        elif choice == "2":
            show_progress()

        elif choice == "3":
            print("Good luck with the job hunt!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
