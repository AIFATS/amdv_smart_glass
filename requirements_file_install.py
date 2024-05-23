import subprocess
import sys

def install_requirements(requirements_file):
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', requirements_file], check=True)
        print(result.stdout)
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        sys.exit(1)
