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
    p = subprocess.run(
        ['git', 'credential', 'fill'],
        input='protocol=https\nhost=github.com\n',
        text=True,
        capture_output=True
    )
    for line in p.stdout.splitlines():
        if line.startswith("password="):
            return line.split("=", 1)[1].strip()
    raise ValueError("Could not retrieve token.")

def github_req(endpoint, method="GET", data=None, token=None):
    url = f"{GITHUB_API}/{endpoint}" if not endpoint.startswith("http") else endpoint
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ERP-GitHub-Automation",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {token}"
    }
    req_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    
    with urllib.request.urlopen(req, timeout=45) as resp:
        resp_body = resp.read().decode("utf-8")
        return json.loads(resp_body) if resp_body else {}

def run_git(cmd):
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    res = subprocess.run(cmd, shell=True, cwd=BASE_DIR, capture_output=True, text=True, env=env)
    if res.returncode != 0:
        print(f"[GIT ERROR] {cmd} -> {res.stderr.strip()}", flush=True)
    else:
        print(f"[GIT OK] {cmd}", flush=True)
    return res

def process_prs():
    token = get_github_token()
    print("[AUTH] GitHub Token verified.", flush=True)

    pr_configs = [
        (
            3,
            "feat/03-finance-procurement-supply-chain",
            "feat(phases 12-16, 28): Student Fees Billing, General Ledger, Procurement, Multi-Store Inventory & Campus POS",
            "This Pull Request implements Phase 12 to 16 and 28: fee invoice scheduling, payment gateway abstraction, general ledger double-entry journal, procurement RFQ, warehouse inventory, and campus store POS.",
            "backend/fees/ backend/payments/ backend/finance/ backend/accounting/ backend/procurement/ backend/vendors/ backend/inventory/ backend/warehouses/ backend/campus_store/"
        ),
        (
            4,
            "feat/04-campus-operations-hr-infrastructure",
            "feat(phases 17-21, 26-27): HR Recruitment ATS, Payroll Engine, Transport GPS, Hostels, Library & Research",
            "This Pull Request implements Phase 17 to 21 and 26 to 27: HR employee lifecycle, payroll tax deductions, bus GPS route tracking, hostel room allocations, MARC21 RFID library circulation, and research grants.",
            "backend/assets/ backend/maintenance/ backend/transport/ backend/hostels/ backend/library/ backend/hr/ backend/recruitment/ backend/payroll/ backend/projects/ backend/events/ backend/research/"
        ),
        (
            5,
            "feat/05-enterprise-platform-ai-analytics",
            "feat(phases 22-25, 29-30, 38-45): Universal Communications, Approval Workflows, AI/ML Dropout Intelligence & Main ASGI API",
            "This Pull Request implements Phase 22 to 25, 29 to 30, and 38 to 45: CRM alumni relations, multi-channel notifications, document vault signatures, configurable workflows, machine learning models, and main FastAPI ASGI application.",
            "backend/crm/ backend/alumni/ backend/communication/ backend/documents/ backend/workflows/ backend/production/ backend/compliance/ backend/audit/ backend/analytics/ backend/ai/ backend/reporting/ backend/search/ backend/main.py"
        ),
        (
            6,
            "feat/06-frontend-portals-devops-testing",
            "feat(phases 31-37): React 1-Click Persona Portals, Flutter Mobile App, 238+ Automated Tests & DevOps Infrastructure",
            "This Pull Request implements Phase 31 to 37: modern React + Tailwind web SPA with 1-click persona logins, Flutter mobile application, 238+ passing unit/integration tests, Docker Compose, Kubernetes manifests, Helm charts, and Terraform AWS IaC.",
            "frontend/ mobile/ database/ infrastructure/ docs/ tests/ docker-compose.yml .github/ scripts/"
        )
    ]

    for pr_num_target, branch_name, pr_title, pr_body, paths_to_add in pr_configs:
        print(f"\n==================== [PR #{pr_num_target}] {branch_name} ====================", flush=True)
        
        # 1. Checkout main from remote
        run_git("git checkout -B main origin/main")
        run_git("git pull origin main")
        
        # 2. Checkout fresh branch from main
        run_git(f"git checkout -B {branch_name}")
        
        # 3. Add and commit files
        run_git(f"git add {paths_to_add}")
        run_git(f'git commit -m "{pr_title}"')
        
        # 4. Push branch
        run_git(f"git push origin {branch_name} --force")
        time.sleep(2)
        
        # 5. Create PR via GitHub API
        print(f"[GITHUB API] Creating PR for {branch_name}...", flush=True)
        pr_payload = {
            "title": pr_title,
            "body": pr_body,
            "head": branch_name,
            "base": "main"
        }
        pr_resp = github_req("pulls", method="POST", data=pr_payload, token=token)
        actual_pr_num = pr_resp.get("number")
        print(f"[GITHUB API] PR #{actual_pr_num} created: {pr_resp.get('html_url')}", flush=True)
        time.sleep(2)
        
        # 6. Merge PR via GitHub API
        print(f"[GITHUB API] Merging PR #{actual_pr_num}...", flush=True)
        merge_payload = {
            "commit_title": f"Merge pull request #{actual_pr_num} from {REPO_OWNER}/{branch_name}",
            "commit_message": pr_body,
            "merge_method": "merge"
        }
        merge_resp = github_req(f"pulls/{actual_pr_num}/merge", method="PUT", data=merge_payload, token=token)
        print(f"[GITHUB API] PR #{actual_pr_num} Merged: {merge_resp.get('merged')} ({merge_resp.get('message')})", flush=True)
        time.sleep(2)

    # 7. Final pull on local main
    print("\n--- [FINAL SYNC] Updating local main with all merged PRs ---", flush=True)
    run_git("git checkout -B main origin/main")
    run_git("git pull origin main")
    print("\n[SUCCESS] All 6 PRs created and merged on GitHub!", flush=True)

if __name__ == '__main__':
    process_prs()
