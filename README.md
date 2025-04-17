# Python_Codes

from datetime import datetime

readme_path = "README.md"

with open(readme_path, "w") as f:
    f.write(f"# My Project\n\n")
    f.write(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
