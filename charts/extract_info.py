import os
import pathlib
import json

rootpath = pathlib.Path(__file__).parent.parent

def collect_exps(path=None):
    path = pathlib.Path(rootpath, "target", "criterion") if path is None else path
    L = list(os.walk(path))
    L = list(filter(lambda e:"benchmark.json" in e[2] and "new" in e[0], L))
    exps = []
    for upath, _, docs in L:
        p = pathlib.Path(upath, "benchmark.json")
        with open(p) as f:
            d = json.load(f)
            exps.append(d)
        p = pathlib.Path(upath, "estimates.json")
        with open(p) as f:
            t = json.load(f)
            d["estimates"] = {
            "mean": [
                t["mean"]["point_estimate"],
                t["mean"]["standard_error"]
            ],
            "median": [
                t["median"]["point_estimate"],
                t["median"]["standard_error"]
            ]
            }
    return exps

def get_exp_data(path=None):
    exps = collect_exps(path=path)
    groups = {}
    for e in exps:
        fname = e["function_id"]
        if fname not in ("rsonpath", "jsonski", "jsurfer"):
            continue
        groups[e["group_id"]] = L = groups.get(e["group_id"], {})
        L[fname] = e
    return groups

def get_dataset():
    datapath = pathlib.Path(rootpath, "data")
    it = os.walk(datapath)
    for directory,_,fs in it:
        for filename in fs:
            if filename.endswith(".json"):
                p = pathlib.Path(directory, filename)
                yield p

def get_query_names():
    d = get_exp_data()
    exps = list(sorted(d))
    exps_short = [f"{exps[i][0].upper()}{i}" for i in range(len(exps))]
    return exps_short, exps
