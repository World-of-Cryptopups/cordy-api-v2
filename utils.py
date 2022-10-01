from typing import Any, Dict


WARRIOR_PUPS = 3000
KNIGHT_PUPS = 5000
OVERLORD_PUPS = 8000
PUPS_OF_THE_APOCALYPSE = 10000
PUPS_ABOVE_ALL = 25000
DOGGOS_OF_INFINITY = 70000
DOGGOS_OF_ENTERNITY = 145000


def identify_dps_role(data: Dict[str, Any]):
    dps: int = data["pupitems"]["real"] + data["puppycards"] + data["pupskincards"]

    if dps >= WARRIOR_PUPS and dps < KNIGHT_PUPS:
        return "Warrior Pups"
    if dps >= KNIGHT_PUPS and dps < OVERLORD_PUPS:
        return "Knight Pups"
    if dps >= OVERLORD_PUPS and dps < PUPS_OF_THE_APOCALYPSE:
        return "Overlord Pups"
    if dps >= PUPS_OF_THE_APOCALYPSE and dps < PUPS_ABOVE_ALL:
        return "Pups of the Apocalypse"
    if dps >= PUPS_ABOVE_ALL and dps < DOGGOS_OF_INFINITY:
        return "Pups Above All"
    if dps >= DOGGOS_OF_INFINITY and dps < DOGGOS_OF_ENTERNITY:
        return "Doggos of Infinity"
    if dps >= DOGGOS_OF_ENTERNITY:
        return "Doggos of Eternity"

    return ""
