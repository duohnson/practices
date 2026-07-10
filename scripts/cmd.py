import subprocess

subprocess.run(
    ["cmd", "/c", "ipconfig"],
    check=True
)