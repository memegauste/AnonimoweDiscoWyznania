"""Various utils made for AnonimoweDiscoWyznania."""
import json
import os
import subprocess


def read_json_file(path):
    """Returns dict from json file."""
    with open(path, 'r', encoding='utf-8') as f:
        json_dict = json.load(f)
    return json_dict


def init_file_existence(path):
    """Check file existence, if not, create it."""
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)


def get_commit_version():
    """Return SHORT commit number."""
    return subprocess.check_output(
        ['git', 'log', '--format="%H"', '-n 1'],
    ).decode('ascii').replace('"', '')[:7]
