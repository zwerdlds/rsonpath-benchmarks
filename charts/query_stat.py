import json
import os
import pathlib
from extract_info import *
import subprocess
import sys

exp_data = get_exp_data()
short_exps, exps = get_query_names()
datasets = {e.parent.name:e for e in get_dataset()}
queries = []
for i in range(len(exps)):
    queries.append((short_exps[i], exp_data[exps[i]]["rsonpath"]["value_str"], exps[i].split("_")[0]))
binary = pathlib.Path(rootpath.parent, "rsonpath", "target", "release", "rsonpath")
print(binary)
print("short name", "match", "query", sep="&\t", end="\\\\\n")
print("\\hline")
for t in queries:
    p = subprocess.Popen([str(binary), "-r", "count", str(t[1]), str(datasets[t[2]])], stdout=subprocess.PIPE)
    query = "\\texttt{"+t[1].replace("$", "\\$").replace("_","\_")+"}"
    print(t[0], query, p.stdout.read().decode().strip(), sep="&\t", end="\\\\\n")
