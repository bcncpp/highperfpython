#!/usr/bin/env python
import pstats
p = pstats.Stats("profile.stats")
p.sort_stats("cumulative")
p.print_stats()