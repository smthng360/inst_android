import os
import json


def write_response(response, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    payload = {
        "url": response.url,
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "json": None,
        "text": None,
    }

    try:
        payload["json"] = response.json()
    except ValueError:
        payload["text"] = response.text

    out_path = os.path.join(out_dir, "submiter.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return out_path


def read_response(input_dir):
    in_path = os.path.join(input_dir, "response_debug.json")
    with open(in_path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return payload


def load_ig_variables(variables_str: str) -> dict:
    import json

    obj = json.loads(variables_str)
    obj = json.loads(obj["params"]["params"])
    obj = json.loads(obj["params"])
    server_params = obj["server_params"]

    return obj
