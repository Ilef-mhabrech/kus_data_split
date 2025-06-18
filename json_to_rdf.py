import os
import json
import re
from rdflib import Graph, Literal, Namespace, URIRef

# Dossiers
input_dir = 'cs_core_split'
output_dir = 'cs_core_rdf'
os.makedirs(output_dir, exist_ok=True)

# Namespace personnalisé
EX = Namespace("http://example.org/ku/")

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

            # Créer le graphe RDF
            g = Graph()
            g.bind("ex", EX)

            # URI basé sur un titre nettoyé
            ku_id = re.sub(r'[^\w\-]', '_', title)
            ku_uri = URIRef(EX + ku_id)

            g.add((ku_uri, EX.title, Literal(title)))
            g.add((ku_uri, EX.csCore, Literal(cs_core)))

            # Enregistrer en .ttl
            output_path = os.path.join(output_dir, f"{ku_id}.ttl")
            g.serialize(destination=output_path, format="turtle")

            count += 1

print(f"✅ Conversion terminée : {count} fichiers RDF générés dans '{output_dir}'.")
