import json
import os
import re

# Charger le fichier JSON principal
with open('data/kus.json', 'r', encoding='utf-8') as f:
    kus = json.load(f)

# Créer le dossier racine de sortie
base_output_dir = 'output/kus_split'
os.makedirs(base_output_dir, exist_ok=True)

# Pour chaque KU, créer un dossier et y placer les 4 fichiers
for ku in kus:
    # Nettoyer le nom de dossier (nom de la KU)
    title = re.sub(r'[^\w\-_.]', '_', ku.get("title", "Unknown_Title"))

    # Créer un sous-dossier pour cette KU
    ku_dir = os.path.join(base_output_dir, title)
    os.makedirs(ku_dir, exist_ok=True)

    # CS Core
    cs_core = {
        "title": ku.get("title"),
        "CS Core": ku.get("CS Core", "")
    }
    with open(os.path.join(ku_dir, f'{title}_cs_core.json'), 'w', encoding='utf-8') as f:
        json.dump(cs_core, f, ensure_ascii=False, indent=2)

    # KA Core
    ka_core = {
        "title": ku.get("title"),
        "KA Core": ku.get("KA Core", "")
    }
    with open(os.path.join(ku_dir, f'{title}_ka_core.json'), 'w', encoding='utf-8') as f:
        json.dump(ka_core, f, ensure_ascii=False, indent=2)

    # Non-core
    non_core = {
        "title": ku.get("title"),
        "Non-core": ku.get("Non-core", "")
    }
    with open(os.path.join(ku_dir, f'{title}_non_core.json'), 'w', encoding='utf-8') as f:
        json.dump(non_core, f, ensure_ascii=False, indent=2)

    # Illustrative Learning Outcomes
    ilo = {
        "title": ku.get("title"),
        "Illustrative Learning Outcomes": ku.get("Illustrative Learning Outcomes", "")
    }
    with open(os.path.join(ku_dir, f'{title}_ilo.json'), 'w', encoding='utf-8') as f:
        json.dump(ilo, f, ensure_ascii=False, indent=2)

print("✅ Séparation terminée. Les fichiers sont regroupés par dossier dans 'output/kus_split'.")
