# kus_data_split

Ce répertoire contient un script Python permettant de **séparer un fichier JSON contenant plusieurs "Knowledge Units" (KUs)** en plusieurs fichiers individuels, organisés par section.
j'ai télécharger le fichier ".JSON" (dans data ) qui contient tout les kUs du répertoire BOK-KG . 

Chaque KU est divisée en quatre parties :
- `CS Core`
- `KA Core`
- `Non-core`
- `Illustrative Learning Outcomes`

Le script crée un dossier par KU, contenant un fichier `.json` pour chacune de ces sections.

---

## 📂 commande
```python3 kus_split.py

