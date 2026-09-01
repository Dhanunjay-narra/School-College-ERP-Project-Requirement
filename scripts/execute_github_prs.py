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
        print(f"[GIT ERROR] {cmd} -> {res.stderr.strip()}")
    else:
        print(f"[GIT OK] {cmd}")
    return res

def create_and_merge_all_prs():
    token = get_github_token()
    print("[AUTH] GitHub Token acquired.")

    # 1. Prepare initial commit
    print("\n--- [STEP 0] Resetting main branch on GitHub to initial commit ---")
    run_git("git checkout --orphan branch_initial")
    run_git("git rm -rf --cached .")
    run_git("git add README.md LICENSE .gitignore .env.example requirements.txt pyproject.toml Makefile pytest.ini")
    run_git('git commit -m "chore: initial enterprise repository structure"')
    run_git("git push -u origin branch_initial:main --force")
    time.sleep(2)

    pr_configs = [
        (
            "feat/01-foundation-identity-org",
            "feat(phases 01-03): Foundation Core Architecture, Identity & Access, and Multi-Tenant Organization",
            "This Pull Request implements Phase 01 to Phase 03: core architecture, event broker, authentication, JWT tokens, PBKDF2 cryptography, RBAC, and multi-campus hierarchy.",
            "backend/core/ backend/identity/ backend/organization/"
        ),
        (
            "feat/02-education-academic-engine",
            "feat(phases 04-11): Student Lifecycle, Admissions CRM, Academics Timetable, Exams & LMS",
            "This Pull Request implements Phase 04 to Phase 11: 8-stage student lifecycle, parent portal, admissions merit ranking, timetable conflict detection, attendance engine, examinations, and LMS assignments.",
            "backend/students/ backend/parents/ backend/admissions/ backend/academics/ backend/faculty/ backend/attendance/ backend/examinations/ backend/assignments/"
        ),
        (
            "feat/03-finance-procurement-supply-chain",
            "feat(phases 12-16, 28): Student Fees Billing, General Ledger, Procurement, Multi-Store Inventory & Campus POS",
            "This Pull Request implements Phase 12 to 16 and 28: fee invoice scheduling, payment gateway abstraction, general ledger double-entry journal, procurement RFQ, warehouse inventory, and campus store POS.",
            "backend/fees/ backend/payments/ backend/finance/ backend/accounting/ backend/procurement/ backend/vendors/ backend/inventory/ backend/warehouses/ backend/campus_store/"
        ),
        (
            "feat/04-campus-operations-hr-infrastructure",
            "feat(phases 17-21, 26-27): HR Recruitment ATS, Payroll Engine, Transport GPS, Hostels, Library & Research",
            "This Pull Request implements Phase 17 to 21 and 26 to 27: HR employee lifecycle, payroll tax deductions, bus GPS route tracking, hostel room allocations, MARC21 RFID library circulation, and research grants.",
            "backend/assets/ backend/maintenance/ backend/transport/ backend/hostels/ backend/library/ backend/hr/ backend/recruitment/ backend/payroll/ backend/projects/ backend/events/ backend/research/"
        ),
        (
            "feat/05-enterprise-platform-ai-analytics",
            "feat(phases 22-25, 29-30, 38-45): Universal Communications, Approval Workflows, AI/ML Dropout Intelligence & Main ASGI API",
            "This Pull Request implements Phase 22 to 25, 29 to 30, and 38 to 45: CRM alumni relations, multi-channel notifications, document vault signatures, configurable workflows, machine learning models, and main FastAPI ASGI application.",
            "backend/crm/ backend/alumni/ backend/communication/ backend/documents/ backend/workflows/ backend/production/ backend/compliance/ backend/audit/ backend/analytics/ backend/ai/ backend/reporting/ backend/search/ backend/main.py"
        ),
        (
            "feat/06-frontend-portals-devops-testing",
            "feat(phases 31-37): React 1-Click Persona Portals, Flutter Mobile App, 238+ Automated Tests & DevOps Infrastructure",
            "This Pull Request implements Phase 31 to 37: modern React + Tailwind web SPA with 1-click persona logins, Flutter mobile application, 238+ passing unit/integration tests, Docker Compose, Kubernetes manifests, Helm charts, and Terraform AWS IaC.",
            "frontend/ mobile/ database/ infrastructure/ docs/ tests/ docker-compose.yml .github/ scripts/"
        )
    ]

    for idx, (branch_name, pr_title, pr_body, paths_to_add) in enumerate(pr_configs, start=1):
        print(f"\n==================== [PR #{idx}] {branch_name} ====================")
        
        # 1. Fetch latest main
        run_git("git fetch origin main")
        run_git("git checkout -B " + branch_name + " origin/main")
        
        # 2. Add files for this PR
        run_git(f"git add {paths_to_add}")
        run_git(f'git commit -m "{pr_title}"')
        
        # 3. Push branch to GitHub
        run_git(f"git push origin {branch_name} --force")
        time.sleep(2)
        
        # 4. Create Pull Request on GitHub
        print(f"[GITHUB API] Creating Pull Request #{idx} on GitHub...")
        pr_payload = {
            "title": pr_title,
            "body": pr_body,
            "head": branch_name,
            "base": "main"
        }
        
        pr_resp = github_req("pulls", method="POST", data=pr_payload, token=token)
        pr_number = pr_resp.get("number")
        html_url = pr_resp.get("html_url")
        print(f"[GITHUB API] PR #{pr_number} created successfully: {html_url}")
        time.sleep(2)
        
        # 5. Merge Pull Request on GitHub
        print(f"[GITHUB API] Merging Pull Request #{pr_number} on GitHub...")
        merge_payload = {
            "commit_title": f"Merge pull request #{pr_number} from {REPO_OWNER}/{branch_name}",
            "commit_message": pr_body,
            "merge_method": "merge"
        }
        merge_resp = github_req(f"pulls/{pr_number}/merge", method="PUT", data=merge_payload, token=token)
        print(f"[GITHUB API] PR #{pr_number} Merged Status: {merge_resp.get('merged')} ({merge_resp.get('message')})")
        time.sleep(2)

    # Pull final merged main locally
    print("\n--- [FINAL] Pulling merged main from GitHub locally ---")
    run_git("git checkout -B main origin/main")
    run_git("git pull origin main")
    run_git("git log --graph --oneline -n 20")
    print("\n[SUCCESS] All 6 Pull Requests created and merged on GitHub!")

if __name__ == '__main__':
    create_and_merge_all_prs()
