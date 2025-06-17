import requests
import json
import os
from datetime import datetime

# Configuration
LINKEDIN_DATA_FILE = 'linkedin_data.json'
GITHUB_API_URL = 'https://api.github.com/repos/lerin17/linkedin-resume-sync/contents/resume.json'
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Store this securely in your environment variables

# Simulated function to get latest LinkedIn data (placeholder)
def get_latest_linkedin_data():
    # In production, you'd scrape or use API.
    # This is simulated for now.
    return {
        "name": "Soetan Adedeji Alabi",
        "title": "Cybersecurity Analyst | GRC | Python",
        "skills": ["GRC", "Security+", "Splunk", "ISO 27001", "Python"],
        "last_updated": datetime.utcnow().isoformat()
    }

# Load old data if it exists
def load_existing_data():
    if os.path.exists(LINKEDIN_DATA_FILE):
        with open(LINKEDIN_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save new data locally
def save_data(data):
    with open(LINKEDIN_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Compare data snapshots
def has_changed(old, new):
    return json.dumps(old, sort_keys=True) != json.dumps(new, sort_keys=True)

# Push update to GitHub
def push_to_github(new_data):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    # Get the existing file's SHA (required by GitHub to update)
    response = requests.get(GITHUB_API_URL, headers=headers)
    if response.status_code == 200:
        sha = response.json()["sha"]
    else:
        sha = None

    message = f"Resume update {datetime.utcnow().isoformat()}"
    content = json.dumps(new_data, indent=4).encode("utf-8")
    encoded_content = content.decode("utf-8")

    payload = {
        "message": message,
        "content": encoded_content.encode("utf-8").decode("utf-8"),
    }

    if sha:
        payload["sha"] = sha

    response = requests.put(GITHUB_API_URL, headers=headers, json=payload)

    if response.status_code in [200, 201]:
        print("✅ GitHub updated successfully.")
    else:
        print("❌ Failed to update GitHub:", response.status_code, response.text)

# Main sync logic
def main():
    print("🔄 Starting resume sync check...")
    new_data = get_latest_linkedin_data()
    old_data = load_existing_data()

    if has_changed(old_data, new_data):
        print("📈 Detected changes. Syncing...")
        save_data(new_data)
        push_to_github(new_data)
    else:
        print("✅ No changes detected. Resume is up-to-date.")

if __name__ == "__main__":
    main()

