import os

os.system("python scripts/extract.py")
os.system("python scripts/transform.py")
os.system("python scripts/load.py")

print("Pipeline completo executado!")