# kus_data_split

Ce répertoire contient des scripts Python permettant de traiter un fichier JSON contenant plusieurs "Knowledge Units" (KUs) issues du répertoire BOK-KG.

📥 J’ai téléchargé le fichier `kus.json` (placé dans le dossier `data/`) qui contient toutes les KUs, chacune composée de 4 sections :
- `CS Core`
- `KA Core`
- `Non-core`
- `Illustrative Learning Outcomes`

---

## 🧰 Scripts inclus

### 🔹 `kus_split.py`
Sépare chaque KU en quatre fichiers `.json`, un par section, et les place dans un sous-dossier unique pour chaque KU dans `data/kus_split/`.

➡️ **Commande :**
```bash
python3 kus_split.py
```

🔹  `split_cs_core_to_files.py`
Extrait uniquement les sections CS Core de chaque KU depuis le fichier kus.json et enregistre un fichier .json individuel par KU dans le dossier cs_core_split/.

➡️ **Commande :**

```bash
python3 split_cs_core_to_files.py
```
🔹 'json_to_rdf.py'
Convertit chaque fichier .json contenant un CS Core (généré dans cs_core_split/) en un fichier RDF Turtle (.ttl), stocké dans cs_core_rdf/.

➡️ **Commande :**
```bash
python3 json_to_rdf.py 
```

📦 Résultat des traitements
output/kus_split/ : contient les 4 fichiers .json par KU

cs_core_split/ : contient un fichier .json par KU avec uniquement le CS Core

cs_core_rdf/ : contient un fichier .ttl par KU avec le graphe RDF (URI, titre, csCore)

💡 Dépendances
Installe les dépendances dans un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
pip install rdflib
```