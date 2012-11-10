import random
random.seed()
from random import randrange
import re
import yaml


def load_data():
    yaml_file = open('data.yaml')
    data = yaml.safe_load(yaml_file)
    yaml_file.close()
    return (data["stems"], data["ontology"])


def pickrandom(group):
    random.seed()
    return group[randrange(len(group)) - 1]

pattern = re.compile(r"<[a-z]*>")


def nodes(stem):
    return pattern.findall(stem)


def find(ontology, node):
    return pickrandom(ontology[node[1:-1]])


def parse(stem, ontology):
    for node in nodes(stem):
        stem = stem.replace(node, find(ontology, node), 1)
        stem = parse(stem, ontology)
    return stem


def suggestion():
    stems, ontology = load_data()
    return parse(pickrandom(stems), ontology)

