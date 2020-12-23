# Updated cache script based on mcadmin.
# Includes timelog toggle so dates are not
# logged at all.
import json
import time
import sys
import errno
from pathlib import Path

class JCache:
    def __init__(self, cachefolder='src/cache/', timelog=False):
        self.cachefolder = cachefolder
        self.timelog = timelog
        try:
            Path(cachefolder).mkdir(parents=True, exist_ok=True)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def stash(self, key, data):
        key = str(key)
        today = time.strftime("%x")
        try:
            with open(self.cachefolder + key + ".json") as cache:
                _cache = json.load(cache)
        except:
            _cache = {}

        if self.timelog:
            _cache[today] = data
        else:
            _cache = data

        with open(self.cachefolder + key + ".json", "w") as cache:
            json.dump(_cache, cache, indent=4)


    def fetch(self, key, range="today"):
        key = str(key)
        today = time.strftime("%x")
        try:
            with open(self.cachefolder + key + ".json") as cache:
                _data = json.load(cache)

            if self.timelog:
                if range == "today":
                    return _data[today]
                if range == "all":
                    return _data
                else:
                    return _data[range]
            else:
                return _data
        except Exception:
            raise Exception("Cache with key " + key + " not found in Cachfolder " + self.cachefolder)
