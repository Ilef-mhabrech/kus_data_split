import os
import json
import re

# Charger le fichier global des KUs
with open('data/kus.json', 'r', encoding='utf-8') as f:
    kus = json.load(f)

# Dossier de sortie
output_dir = 'cs_core_split'
os.makedirs(output_dir, exist_ok=True)

# Traitement de chaque KU
count = 0
for ku in kus:
    title = ku.get("title")
    cs_core = ku.get("CS Core")

    if title and cs_core:
        # Nettoyage du nom de fichier
        filename_safe = re.sub(r'[^\w\-_.]', '_', title)
        filename = f"{filename_safe}_cs_core.json"
        filepath = os.path.join(output_dir, filename)

        # Écriture du fichier
        with open(filepath, 'w', encoding='utf-8') as f_out:
            json.dump({
                "title": title,
                "CS Core": cs_core
            }, f_out, ensure_ascii=False, indent=2)

        count += 1

print(f"✅ {count} fichiers CS Core créés dans le dossier '{output_dir}'.")
