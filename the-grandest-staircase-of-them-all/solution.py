import functools
import collections

"""ADAPTED FROM https://stackoverflow.com/a/18723434 to replicate functools.lru_cache functionality available in Python 3"""
def lru_cache(maxsize=255):
    class _LRU_Cache_class(object):
        def __init__(self, input_func, max_size):
            self._input_func = input_func
            self._max_size = max_size
            self._caches_dict = {}

        def cache_clear(self, caller=None):
            if caller in self._caches_dict:
                del self._caches_dict[caller]
                self._caches_dict[caller] = [collections.OrderedDict()]

        def __get__(self, obj, objtype):
            return_func = functools.partial(self._cache_wrapper, obj)
            return_func.cache_clear = functools.partial(self.cache_clear, obj)
            return functools.wraps(self._input_func)(return_func)

        def __call__(self, *args, **kwargs):
            return self._cache_wrapper(None, *args, **kwargs)

        __call__.cache_clear = cache_clear

        def _cache_wrapper(self, caller, *args, **kwargs):
            kwargs_key = "".join(map(lambda x: str(x) + str(type(kwargs[x])) + str(kwargs[x]), sorted(kwargs)))
            key = "".join(map(lambda x: str(type(x)) + str(x), args)) + kwargs_key

            if caller not in self._caches_dict:
                self._caches_dict[caller] = [collections.OrderedDict()]

            cur_caller_cache_dict = self._caches_dict[caller][0]
            if key in cur_caller_cache_dict:
                return cur_caller_cache_dict[key]

            if self._max_size and len(cur_caller_cache_dict) >= self._max_size:
                cur_caller_cache_dict.popitem(False)

            cur_caller_cache_dict[key] = self._input_func(caller, *args,
                                                          **kwargs) if caller != None else self._input_func(*args,
                                                                                                            **kwargs)
            return cur_caller_cache_dict[key]

    return lambda input_func: functools.wraps(input_func)(_LRU_Cache_class(input_func, maxsize))


@lru_cache(maxsize=None)
def get_permutations_of_steps(lower, higher):
    total = 0
    for new_lower in range(lower + 1, higher + 1):
        new_higher = higher - new_lower
        if new_lower < new_higher:
            total += get_permutations_of_steps(new_lower, new_higher) + 1
    return total


def solution(n):
    initial_splits = [(x, n - x) for x in range(1, n // 2 + 1) if x < n - x]
    return sum(get_permutations_of_steps(*split) + 1 for split in initial_splits)
