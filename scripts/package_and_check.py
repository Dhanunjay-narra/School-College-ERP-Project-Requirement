import os
import sys
import zipfile
import json
import urllib.request
import urllib.error
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ZIP_NAME = "School-College-ERP-Project-Requirement.zip"
CHECKER_URL = "https://train-plex-checker-bot-1--ttejaswar1234.replit.app/api/check"

def create_zip():
    zip_path = BASE_DIR / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()
        
    print(f"[ZIP] Creating archive: {zip_path.name} (including .git)...")
    
    total_files = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(BASE_DIR):
            # Ignore transient cache directories
            if "node_modules" in root or "__pycache__" in root or ".pytest_cache" in root or "uploads" in root:
                continue
            for f in files:
                if f.endswith(".zip") or f.endswith(".log") or f == ".env":
                    continue
                file_path = Path(root) / f
                rel_path = file_path.relative_to(BASE_DIR)
                zipf.write(file_path, str(rel_path))
                total_files += 1

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    print(f"[ZIP] Archive created successfully: {total_files} files, {size_mb:.2f} MB")
    return zip_path

def upload_and_verify(zip_path):
    print(f"[CHECKER] Submitting {zip_path.name} to TrainPlex Checker Bot ({CHECKER_URL})...")
    
    boundary = "----WebKitFormBoundaryERP2026CheckerUpload"
    c_type = f"multipart/form-data; boundary={boundary}"
    
    with open(zip_path, "rb") as f:
        file_bytes = f.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{zip_path.name}"\r\n'
        f"Content-Type: application/zip\r\n\r\n"
    ).encode("utf-8") + file_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = urllib.request.Request(CHECKER_URL, data=body, headers={"Content-Type": c_type})
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw_res = resp.read().decode("utf-8")
            result = json.loads(raw_res)
            print("\n================ TRAINPLEX CHECKER BOT RESULTS ================")
            print(json.dumps(result, indent=2))
            print("===============================================================\n")
            
            score = result.get("score") or result.get("total_score") or result.get("pass_rate")
            print(f"[RESULT SCORE]: {score}")
            return result
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"[CHECKER HTTP ERROR]: {e.code} - {err_msg}")
        return None
    except Exception as ex:
        print(f"[CHECKER ERROR]: {ex}")
        return None

if __name__ == '__main__':
    z = create_zip()
    upload_and_verify(z)
