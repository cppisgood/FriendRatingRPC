import logging
import json
import requests
from crawler.codeforces.thread_pool_executor import CODEFORCES_THREAD_EXECUTOR


def get_codeforces_contest_data(handle: str) -> dict:
    logging.info(f'crawling codeforces handle: {handle}')
    try:
        task = CODEFORCES_THREAD_EXECUTOR.submit(requests.get,
                                                 f"https://codeforces.com/api/user.rating?handle={handle}")
        result = json.loads(task.result().text)
        result["data"] = []
        for contest in result["result"]:
            cur = dict()
            cur["rating"] = contest["newRating"]
            cur["timestamp"] = contest["ratingUpdateTimeSeconds"]
            cur["url"] = "https://codeforces.com/contest/" + str(contest["contestId"])
            cur["name"] = contest["contestName"]
            result["data"].append(cur)
        del result["result"]
        result["handle"] = handle
        result["profile_url"] = f"https://codeforces.com/profile/{handle}"
        result["length"] = len(result["data"])
        if len(result["data"]):
            result["rating"] = result["data"][-1]["rating"]
        return result
    except Exception as e:
        logging.exception(e)
        return {
            "status": "unknown error",
            "data": [],
        }


if __name__ == '__main__':
    print(get_codeforces_contest_data("ConanYu"))
