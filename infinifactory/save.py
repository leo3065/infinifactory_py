from . import world_blocks

from typing import List, Dict, Any

def convert_value_by_key_value(keys: List[str], value: str) -> Any:
    handlers_by_first_key = {
        'InputRate': int,
        'Solution': lambda v: world_blocks.WorldBlocks.from_base64_string(v) if v else None,
        'Options': lambda v: value == 'True' if v in ['True', 'False'] else int(v),
    }
    handlers_by_last_key = {
        'Blocks': int,
        'Cycles': int,
        'Footprint': int,
    }
    if keys[0] in handlers_by_first_key:
        return handlers_by_first_key[keys[0]](value)
    if keys[-1] in handlers_by_last_key:
        return handlers_by_last_key[keys[-1]](value)
    if value in ['True', 'False']:
        return value == 'True'
    return value

def save_data_read(file_path: str) -> Dict[str, Any]:
    """Reads the save data from a file. The format of the save data is as follows:
    For each line: 
        <keys>[.<subkeys>]+ = <value>

    Args:
        file_path: The path to the save file.

    Returns:
        The contents of the save file as nested dictionaries.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        result = {}
        for line in file.read().splitlines():
            key, value = line.split(" = ")
            keys = key.split(".")
            curr_dict = result
            for k in keys[:-1]:
                curr_dict = curr_dict.setdefault(k, {})
            curr_dict[keys[-1]] = convert_value_by_key_value(keys, value)
    return result
