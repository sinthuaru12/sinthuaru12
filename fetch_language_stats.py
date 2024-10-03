import json
import os

# Load the list of repositories
with open('repos.json', 'r') as f:
    repos = json.load(f)

languages = {}

# Get language stats for each repository
for repo in repos:
    repo_name = repo['full_name']
    os.system(f"curl -H 'Authorization: token {os.getenv('GITHUB_TOKEN')}' \
    https://api.github.com/repos/{repo_name}/languages > temp_lang.json")
    
    # Load language stats for the current repository
    with open('temp_lang.json', 'r') as lf:
        lang_stats = json.load(lf)
        for lang, size in lang_stats.items():
            if lang in languages:
                languages[lang] += size
            else:
                languages[lang] = size

# Save aggregated language stats
with open('languages.json', 'w') as lf:
    json.dump(languages, lf)

