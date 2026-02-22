from datetime import datetime, timezone
import json


def time_diffs_ms(reference_ts_ms: int, *timestamps_ms) -> None:
    """
    Shows time differences (in milliseconds and human-readable format)
    relative to the provided reference timestamp.

    Parameters:
        reference_ts_ms: int - main timestamp to compare against (e.g. 1767733471393)
        *timestamps_ms: multiple timestamps to compare with reference

    Example:
        time_diffs_ms(1767733471393, 1767733471753, 1767733471829, 1767733473472)
    """
    ref_dt = datetime.fromtimestamp(reference_ts_ms / 1000, tz=timezone.utc)
    print(f"Reference time: {ref_dt}  ({reference_ts_ms})\n")

    for ts_ms in timestamps_ms:
        dt = datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc)
        diff_ms = ts_ms - reference_ts_ms

        # Human-readable difference
        abs_diff_ms = abs(diff_ms)
        seconds = abs_diff_ms // 1000
        ms = abs_diff_ms % 1000

        direction = "after" if diff_ms >= 0 else "before"
        if seconds == 0:
            readable = f"{ms} ms {direction}"
        elif seconds < 60:
            readable = f"{seconds}.{ms:03d} seconds {direction}"
        elif seconds < 3600:
            minutes = seconds // 60
            secs = seconds % 60
            readable = f"{minutes}m {secs}s {direction}"
        else:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            readable = f"{hours}h {minutes}m {direction}"

        print(f"{ts_ms:13d} → {dt}  |  {diff_ms:+8d} ms  |  {readable}")


def scrape_timestamps_from_file(file_path: str) -> list[int]:
    """
    Scrapes all integer timestamps from a given file.

    Parameters:
        file_path: str - path to the file to scrape timestamps from

    Returns:
        List of integer timestamps found in the file.
    """
    with open(file=file_path) as f:
        data = json.load(f)
