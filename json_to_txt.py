import os
import json
import re

# Dossiers
input_dir = 'output/cs_core_split'
output_dir = 'output/cs_core_txt'
os.makedirs(output_dir, exist_ok=True)

# Traitement de chaque fichier JSON
count = 0
for filename in os.listdir(input_dir):
    if filename.endswith('_cs_core.json'):
        filepath = os.path.join(input_dir, filename)

        with open(filepath, 'r', encoding='utf-8') as f:
            ku_data = json.load(f)
            title = ku_data.get("title", "").strip()
            cs_core = ku_data.get("CS Core", "").strip()

            if not title or not cs_core:
                continue

            # Nettoyage du nom de fichier
            ku_id = re.sub(r'[^\w\-]', '_', title)
            output_path = os.path.join(output_dir, f"{ku_id}.txt")

            # Écriture dans le fichier .txt
            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(f"Title: {title}\n\n")
                txt_file.write("CS Core:\n")
                txt_file.write(cs_core)

            count += 1

print(f"✅ Conversion terminée : {count} fichiers texte générés dans '{output_dir}'.")
