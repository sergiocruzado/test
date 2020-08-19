#!/usr/bin/env python3

import os

from tmdbv3api import TMDb
from tmdbv3api import Movie


tmdb = TMDb()
tmdb.api_key = os.environ['API_KEY']

def main():

 pass

if __name__ == '__main__':
    main()
