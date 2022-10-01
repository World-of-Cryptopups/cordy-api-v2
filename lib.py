from typing import Dict


def calc_dps(data: Dict) -> int:
    return data["pupitems"]["real"] + data["puppycards"] + data["pupskincards"]
