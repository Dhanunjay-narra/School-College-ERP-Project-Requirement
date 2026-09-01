import subprocess
import json
import urllib.request
import urllib.error
import time
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPO_OWNER = "Dhanunjay-narra"
REPO_NAME = "School-College-ERP-Project-Requirement"
GITHUB_API = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

def get_github_token():
    res = subprocess.run(
        'echo "protocol=https\nhost=github.com" | git credential fill',
        shell=True,
        capture_output=True,
        text=True
    )
    for line in res.stdout.splitlines():
        if line.startswith("password="):
            return line.split("=", 1)[1].strip()
    raise ValueError("Could not find GitHub token from git credential manager.")

def github_api_request(endpoint, method="GET", data=None, token=None):
    url = f"{GITHUB_API}/{endpoint}" if not endpoint.startswith("http") else endpoint
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ERP-GitHub-Automation",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    req_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp_body = resp.read().decode("utf-8")
            return json.loads(resp_body) if resp_body else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"[API ERROR] {method} {url} -> HTTP {e.code}: {err_msg}")
        raise

def run_git(cmd):
    res = subprocess.run(cmd, shell=True, cwd=BASE_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[GIT ERROR] {cmd} -> {res.stderr.strip()}")
    return res

def test_api():
    token = get_github_token()
    print(f"[GITHUB AUTH] Token retrieved successfully: {token[:8]}...")
    repo_info = github_api_request("", token=token)
    print(f"[GITHUB REPO] Connected to: {repo_info.get('full_name')} (Private: {repo_info.get('private')})")

if __name__ == '__main__':
    test_api()
