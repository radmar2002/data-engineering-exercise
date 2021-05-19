#!/usr/bin/env python3
"""
data-engineering-exercise
"""

__author__ = "Marius Radu"
__version__ = "0.0.1"

import os
import argparse
import json
import pandas as pd

from logzero import logger
from collections import defaultdict


def list_nester(input_df, n_levels):

    gr_els = list(n_levels)
    n_levels.append("amount")
    df_reduced = input_df[n_levels]
    grouped_reduced = df_reduced.groupby(gr_els).sum()
    #grouped_reduced_toparse = grouped_reduced.to_dict(orient='index')

    results = defaultdict(lambda: defaultdict(dict))

    for index, value in grouped_reduced.itertuples():
        for i, key in enumerate(index):
            if i == 0:
                nested = results[key]
            elif i == len(index) - 1:
                nested[key] = [{'amount': value}]
            else:
                nested = nested[key]

    res = json.dumps(results, indent=4)
    return res


def main(args):
    """ Main entry point of the app """
    # logger.debug("This will nest json array from file with nesting levels:")
    nesting_levels = args.nesting_levels
    # logger.debug(nesting_levels)

    if len(nesting_levels) < 2:
        logger.error("Please enter at least two nesting levels!")
        return False

    with open(args.filename) as inputfile:
        inputdata = json.load(inputfile)

    idata = pd.DataFrame(inputdata)
    #  check if DF columnames contains the nesting leveels
    nl_check = all(elem in list(idata.columns) for elem in nesting_levels)
    if nl_check == False:
        logger.error("The mentioned nesting levels are not included in file")
        return False

    nested_list = list_nester(idata, nesting_levels)

    # logger.info(nested_list)
    # return nested_list
    print(nested_list)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(description="Nest json array from file")

    # Required positional argument
    parser.add_argument(dest="filename",
                        help="Required positional argument")

    parser.add_argument(dest="nesting_levels",
                        help="Required positional argument", nargs="+")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()

    main(args)
