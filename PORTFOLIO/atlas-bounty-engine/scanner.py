import requests
import json

class GitHubScanner:
    """
    Scans GitHub for potential bounty targets based on keywords and labels.
    """
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json"
        }

    def search_bounties(self, query="label:bounty is:open"):
        url = f"https://api.github.com/search/issues?q={query}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get("items", [])
        return []

    def get_issue_details(self, owner, repo, issue_number):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else None
