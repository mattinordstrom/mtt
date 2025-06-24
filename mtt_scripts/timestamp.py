import sys, time
from datetime import datetime

YELLOW = '\033[93m'
ENDC = '\033[0m'

def normalize_to_milliseconds(ts):
    if isinstance(ts, float):
        return int(ts * 1000)
    elif isinstance(ts, int):
        return ts * 1000 if ts < 1e12 else ts
    elif isinstance(ts, str):
        if ts.count('.') == 1:
            parts = ts.split('.')
            if parts[0].isdigit() and parts[1].isdigit():
                return int(parts[0] + parts[1].ljust(3, '0')[:3])
        elif ts.isdigit():
            ts_int = int(ts)
            return ts_int * 1000 if ts_int < 1e12 else ts_int
    raise ValueError(f"Unrecognized timestamp format: {ts}")

def datetime_to_unix_ms(dt_str):
    if "." in dt_str:
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')
    else:
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    timestamp_s = dt.timestamp()
    return int(timestamp_s * 1000)

def convert_unix_to_local_datetime(unix_ts):
    ts_ms = normalize_to_milliseconds(unix_ts)
    dt = datetime.fromtimestamp(ts_ms / 1000.0)
    return dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


print("\n")
if len(sys.argv) > 1:
    ts = sys.argv[1]
else:
    print(YELLOW + str(normalize_to_milliseconds(time.time())) + ENDC)
    exit(0)

input_is_unix_ts = True
if "-" in ts:
    input_is_unix_ts = False


print(ts)
print("\n")

if input_is_unix_ts:
    print(YELLOW + str(convert_unix_to_local_datetime(ts)) + ENDC)
else:
    print(YELLOW + str(datetime_to_unix_ms(ts)) + ENDC)


