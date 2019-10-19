import requests
import json
import datetime
import re


endpoint_address = "https://nrt3.modaps.eosdis.nasa.gov"
app_key = "FCEC8548-F224-11E9-8D49-31F3207B60E0"
time_tuple = datetime.datetime.now().timetuple()
today = "%d%03d" % (time_tuple.tm_year, time_tuple.tm_yday)


def download_index() -> dict:
    response_raw = requests.get(
        f"{endpoint_address}/api/v2/content/details/FIRMS/viirs/South_America",
        params="fields=all&format=json",
        headers={"Authorization": f"Bearer {app_key}"},
    )

    return json.loads(response_raw.content)


def download_viirs_nrt_today(julian_day=today) -> str:
    index_dict = download_index()
    response = b""

    for item in index_dict["content"]:

        if re.search(julian_day, item["name"]):
            print(f"Downloading: {endpoint_address}/{item['downloadsLink']}")
            response = requests.get(
                url=f"{endpoint_address}{item['downloadsLink']}",
                headers={"Authorization": f"Bearer {app_key}"},
            )

    return str(response.content, "utf-8")
