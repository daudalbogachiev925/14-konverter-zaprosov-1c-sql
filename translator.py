import re, yaml

RULES = yaml.safe_load(open('rules.yaml'))

def translate(query_1c: str) -> str:
    q = query_1c
    for ru, en in {**RULES['keywords'], **RULES['functions']}.items():
        q = re.sub(rf'\b{ru}\b', en, q, flags=re.IGNORECASE)
    return q
