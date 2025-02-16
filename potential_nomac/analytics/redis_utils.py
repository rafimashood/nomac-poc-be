import json
from datetime import datetime
import redis
from django.conf import settings


redis_client = redis.StrictRedis(host=settings.REDIS_SERVER,
                                 port=settings.REDIS_PORT,
                                 password=settings.REDIS_PASSWORD, ssl=True, decode_responses=True)

# Function to retrieve all JSON data from Redis
def get_all_cache_data(blocks: list[int], from_date: str, to_date: str, cleaning_event: int) -> list:
    """Retrieve cache data from Redis where keys match the ID prefix 'IR{user_param}_'."""
    records = []
    ploty_data = []

    from_timestamp = int(datetime.strptime(from_date, "%Y-%m-%d").timestamp())
    to_timestamp = int(datetime.strptime(to_date, "%Y-%m-%d").timestamp()) + 86399

    for block in blocks:
        prefix = (f"IR{block}_")
        block_data_map = {"x": [], "y": [], "name": block}

        for key in redis_client.scan_iter(f"{prefix}*"):
            decoded_key = key.decode() if isinstance(key, bytes) else key
            value = redis_client.get(decoded_key)
            try:
                decoded_value = json.loads(value.decode() if isinstance(value, bytes) else value)
            except (json.JSONDecodeError, AttributeError):
                decoded_value = value.decode() if isinstance(value, bytes) else value

            if isinstance(decoded_value, list):
                for item in decoded_value:
                    if from_timestamp <= item.get("timestamp", 0) <= to_timestamp:
                        if cleaning_event == 1 and item.get("cleaning_event") == 1:
                            if len(block_data_map["x"]) < 11 and len(block_data_map["x"]) < 11:
                                    block_data_map["x"].append(item.get("formatted_date"))
                                    block_data_map["y"].append(item.get("current_signal"))
                            records.append(item)
                        else:
                            block_data_map["x"].append(item.get("formatted_date"))
                            block_data_map["y"].append(item.get("current_signal"))
                            # if len(records)<=100:
                            records.append(item)
                            # else:
                            #     break
        block_data_map["x"] = list(set(block_data_map["x"]))
        block_data_map["y"] = list(set(block_data_map["y"]))
        ploty_data.append(block_data_map)
    return records, ploty_data
