import subprocess, urllib.request, json

p = subprocess.run(['git', 'credential', 'fill'], input='protocol=https\nhost=github.com\n', text=True, capture_output=True)
token = None
for line in p.stdout.splitlines():
    if line.startswith('password='):
        token = line.split('=', 1)[1].strip()

req = urllib.request.Request(
    'https://api.github.com/repos/Dhanunjay-narra/School-College-ERP-Project-Requirement/pulls?state=all',
    headers={'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json', 'User-Agent': 'ERP-App'}
)

with urllib.request.urlopen(req) as resp:
    prs = json.loads(resp.read().decode('utf-8'))
    print(f'Total PRs on GitHub: {len(prs)}')
    for pr in prs:
        num = pr["number"]
        title = pr["title"]
        state = pr["state"]
        merged = pr.get("merged_at") is not None
        print(f"#{num}: {title} [{state.upper()}] (Merged: {merged})")
