# main.py
from data_generate import visualize_random_walk
from data_csv import visualize_csv_weather
from data_json import visualize_earthquake
from data_api import visualize_github_repos

def main():
    while True:
        print("\n=== DATA VISUALIZATION PROJECT ===")
        print("1. Generate Data (Random Walk)")
        print("2. Load CSV (Weather)")
        print("3. Load JSON (Earthquake)")
        print("4. Call API (GitHub Repos)")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            visualize_random_walk()
        elif choice == "2":
            visualize_csv_weather()
        elif choice == "3":
            visualize_earthquake()
        elif choice == "4":
            visualize_github_repos()
        elif choice == "0":
            break
        else:
            print("Invalid! Try again.")

if __name__ == "__main__":
    main()
