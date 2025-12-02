import requests
import matplotlib.pyplot as plt


def visualize_github_repos():
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

    response = requests.get(url)
    print("Status:", response.status_code)

    data = response.json()
    repo_names, stars = [], []

    for item in data["items"][:10]:
        repo_names.append(item["name"])
        stars.append(item["stargazers_count"])

    plt.figure(figsize=(11, 5))
    plt.bar(repo_names, stars)
    plt.xticks(rotation=45, ha="right")
    plt.title("Top 10 Python GitHub Repos by Stars")
    plt.xlabel("Repository")
    plt.ylabel("Stars")
    plt.tight_layout()

    plt.savefig("output_github_repos.png")  # Lưu ra file
    print("Saved GitHub Repos plot as output_github_repos.png")
