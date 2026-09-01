import os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def write_f(path_str, text):
    p = BASE / path_str
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text.strip() + '\n')
    print(f'[GEN] Created: {path_str}')

if __name__ == '__main__':
    print('writer_util ready')
