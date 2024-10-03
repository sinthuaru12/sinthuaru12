import json

# Load the language stats
with open('languages.json', 'r') as f:
    languages = json.load(f)

# Calculate the total size for all languages
total_size = sum(languages.values())

# Calculate the percentage for each language
language_percentages = {lang: (size / total_size) * 100 for lang, size in languages.items()}

# Sort languages by percentage
sorted_languages = sorted(language_percentages.items(), key=lambda x: x[1], reverse=True)

# Read the current README file
with open('README.md', 'r') as f:
    readme_lines = f.readlines()

# Define start and end markers for the language section in the README
start_marker = "<!-- LANGUAGES-START -->"
end_marker = "<!-- LANGUAGES-END -->"

start_index = -1
end_index = -1

# Find the indices for the start and end of the language section
for i, line in enumerate(readme_lines):
    if start_marker in line:
        start_index = i
    if end_marker in line:
        end_index = i

# Create the new language section content
new_language_section = [
    "**Most Used Languages (Public + Private Repos):**\n\n",
    "<!-- LANGUAGES-START -->\n"
]

for lang, perc in sorted_languages:
    new_language_section.append(f"- {lang}: {perc:.2f}%\n")

new_language_section.append("<!-- LANGUAGES-END -->\n")

# Replace the old language section with the new one
if start_index != -1 and end_index != -1:
    updated_readme = readme_lines[:start_index] + new_language_section + readme_lines[end_index+1:]
else:
    print("Language section markers not found in README.md.")

# Write the updated content back to the README
with open('README.md', 'w') as f:
    f.writelines(updated_readme)

