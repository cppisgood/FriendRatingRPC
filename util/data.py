from util.scheduler_cache import SchedulerCache
from crawler.atcoder.get_atcoder_contest_data import get_atcoder_contest_data
from crawler.codeforces.get_codeforces_contest_data import get_codeforces_contest_data
from crawler.codeforces.get_codeforces_submit_data import get_codeforces_submit_data
from crawler.nowcoder.get_nowcoder_contest_data import get_nowcoder_contest_data
from crawler.luogu.get_luogu_submit_data import get_luogu_submit_data

ATCODER_RATING_CACHE = SchedulerCache(get_atcoder_contest_data)
CODEFORCES_RATING_CACHE = SchedulerCache(get_codeforces_contest_data)
NOWCODER_RATING_CACHE = SchedulerCache(get_nowcoder_contest_data)
CODEFORCES_SUBMIT_CACHE = SchedulerCache(get_codeforces_submit_data)
LUOGU_SUBMIT_CACHE = SchedulerCache(get_luogu_submit_data)


contest_cache = {
    'atcoder': SchedulerCache(get_atcoder_contest_data),
    'codeforces': SchedulerCache(get_codeforces_contest_data),
    'nowcoder': SchedulerCache(get_nowcoder_contest_data),
}

submit_cache = {
    'codeforces': SchedulerCache(get_codeforces_submit_data),
    'luogu': SchedulerCache(get_luogu_submit_data),
}