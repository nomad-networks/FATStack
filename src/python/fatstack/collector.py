""" The FATStack data server

This process collects and stores trade information from exchanges and serves
it to other FATStack processes.

"""

import fatstack as fs
import fatstack.database as fsdb
import logging
import sys

collector = sys.modules[__name__]
log = logging.getLogger("Collector")


def init(init_string):
    log.info("Initializing collector.")
    fs.ROOT.Sys.collector = collector

    collector.init_string = init_string

    # Setting up the database
    collector.db = fsdb.Database(fs.ROOT.Config.collector_database)

    # Start instrument tracking
    for instrument in fs.ROOT.Config.instruments:
        instrument.start_tracking()

    # Start exchange tracking
    for exchange in fs.ROOT.Config.exchanges:
        exchange.start_tracking(fs.ROOT.Config.instruments)

    log.info("Initialization done.")
    log.debug("ROOT: {}".format(fs.ROOT.ls()))
