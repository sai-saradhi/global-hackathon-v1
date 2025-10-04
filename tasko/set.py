import os

# Base path for your project
base_path = "tasko"

# Define folder structure and files
structure = {
    "app": {
        "main.py": "# Entry point for the FastAPI/Flask app\n",
        "routes": {
            "tasks.py": "# Endpoints for task logging & recommendations\n",
            "users.py": "# Endpoints for user management\n",
        },
        "models": {
            "user.py": "# User DB model\n",
            "task.py": "# Task DB model\n",
        },
        "services": {
            "markov.py": "# Markov chain logic\n",
            "reward.py": "# Reward function logic\n",
            "ml_model.py": "# ML model integration\n",
        },
        "utils": {
            "calendar.py": "# Calendar helpers\n",
            "time_helpers.py": "# Time helper functions\n",
        },
        "templates": {
            "dashboard.html": "<!-- Dashboard page -->\n",
            "login.html": "<!-- Login page -->\n",
            "schedule.html": "<!-- Schedule page -->\n",
            "task_log.html": "<!-- Task log page -->\n",
        },
        "static": {
            "css": {
                "bootstrap.min.css": "/* Bootstrap CSS placeholder */\n",
            },
            "js": {
                "bootstrap.bundle.min.js": "// Bootstrap JS placeholder\n",
                "chart.min.js": "// Chart.js placeholder\n",
            },
            "images": {},
        },
        "db.py": "# Database connection\n",
    },
    "requirements.txt": "# Add your dependencies here\nfastapi\nuvicorn\npandas\nscikit-learn\n",
    "README.md": "# Tasko - Markov Chain + ML Task Scheduler\n",
}

def create_structure(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

create_structure(base_path, structure)
print("Project skeleton created with initial files!")
