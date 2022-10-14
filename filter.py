from typing import Any, Dict, List

from lib import calc_dps


def filter_rankings(data: List[Dict[str, Any]]):
    """
    Rankings and DPS:
        Overlord Pups = 10000 - 20000
        Apocalyptic Pups = 20000 - 35000
        Above All Pups = 35000 - 60000
        Infinity Pups = 60000 - 100000
        Eternity Pups = >=100000

    """

    overlord_pups: List[Dict[str, Any]] = []
    apocalyptic_pups: List[Dict[str, Any]] = []
    aboveall_pups: List[Dict[str, Any]] = []
    infinity_pups: List[Dict[str, Any]] = []
    eternity_pups: List[Dict[str, Any]] = []

    for i in data:
        total_dps = calc_dps(i["dps"])

        # there might be problem in the worker not having the wallet
        if "wallet" not in i:
            continue

        info = {"wallet": i["wallet"], "id": i["id"], "dps": total_dps}

        if total_dps >= 10000 and total_dps < 20000:
            overlord_pups.append(info)

        if total_dps >= 20000 and total_dps < 35000:
            apocalyptic_pups.append(info)

        if total_dps >= 35000 and total_dps < 60000:
            aboveall_pups.append(info)

        if total_dps >= 60000 and total_dps < 100000:
            infinity_pups.append(info)

        if total_dps >= 100000:
            eternity_pups.append(info)

    overlord_pups.sort(key=lambda x: x["dps"], reverse=True)
    apocalyptic_pups.sort(key=lambda x: x["dps"], reverse=True)
    aboveall_pups.sort(key=lambda x: x["dps"], reverse=True)
    infinity_pups.sort(key=lambda x: x["dps"], reverse=True)
    eternity_pups.sort(key=lambda x: x["dps"], reverse=True)

    return {
        "Overlord Pups": overlord_pups,
        "Apocalyptic Pups": apocalyptic_pups,
        "Above All Pups": aboveall_pups,
        "Infinity Pups": infinity_pups,
        "Eternity Pups": eternity_pups,
    }
