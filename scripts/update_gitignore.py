from writer_util import write_f

write_f(".gitignore", """__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.env*
.env
.venv
build/
dist/
node_modules/
.vite/
.DS_Store
*.log
local_data/
uploads/
*.zip
""")
