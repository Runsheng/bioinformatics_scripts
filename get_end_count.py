#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pysam import AlignmentFile


def count_end(pos_d):
    """
    count the end of reads
    """
    end_d = {}
    for k, v in pos_d.items():
        start, end = v
        try:
            end_d[end] += 1
        except KeyError:
            end_d[end] = 1
    return end_d


def count_start(pos_d):
    """
    count the start of the reads
    :param pos_d:
    :return:
    """

    start_d={}
    for k, v in pos_d.items():
        start, end=v
        try:
            start_d[start] += 1
        except KeyError:
            start_d[start] = 1
    return start_d


def filter_end(end_d, min_coverage=2):
    """
    filter end_d with min_coverage
    only merge the sites within the offset 
    """
    end_d_f = {}
    for k, v in end_d.items():
        if v >= min_coverage:
            end_d_f[k] = v
    return end_d_f


def group_end(end_d_f, offset=5):
    """
    only merge the sites within the offset 
    """
    key_s = sorted(end_d_f.keys())
    key_new = []
    # print key_s

    # Make two iterables (think: virtual lists) from one list
    previous_sequence, current_sequence = iter(key_s), iter(key_s)

    # Initialize the groups while advancing current_sequence by 1
    # element at the same time
    groups = [[next(current_sequence)]]

    # Iterate through pairs of numbers
    for previous, current in zip(previous_sequence, current_sequence):
        if abs(previous - current) >= offset:
            # Large gap, we create a new empty sublist
            groups.append([])
        # Keep appending to the last sublist
        groups[-1].append(current)

    # print(groups)

    #### write a dict for number to end

    end_group_d = {}
    for ll in groups:
        last = ll[-1]
        for i in ll:
            end_group_d[i] = last
    return end_group_d


def is_span_site(start, end, site):
    """
    determine if the site is in the read region
    """

    if start <= site < end:
        return True
    else:
        return False


def get_span_number(pos_d, site):
    count = 0
    for k, v in pos_d.items():
        start, end = v
        if is_span_site(start, end, site):
            count += 1
    return count


def scan_span_dic(pos_d, end_d, end_group_d):
    """
    ratio_d, end:(stop, span)
    """

    ratio_d = {}
    for site, stop_count in end_d.items():
        real_site = end_group_d[site]
        span_count = get_span_number(pos_d, real_site)

        try:
            ratio_d[real_site][0] += stop_count
        except KeyError:
            ratio_d[real_site] = [0, span_count]
            ratio_d[real_site][0] += stop_count

    return ratio_d


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bamfile",
                        help="the sorted and indexed bam file")
    parser.add_argument("-e", "--end_coverage", type=int, default=3,
                        help="the min end coverage to be parsed")

    parser.add_argument("-r", "--region_offset", type=int, default=5,
                        help="the offset of end regions to be merged in counting spanning reads")

    parser.add_argument("-c", "--coverage_ratio", type=float, default=0.001,
                        help="the min coverage/count ratio of the end reads and spanning reads to be printed")

    parser.add_argument("-m", "--mode", type=str, default="end",
                        help="count the 3' end or the 5' start can be adjusted using the mode parameter")

    args = parser.parse_args()
    samfile = AlignmentFile(args.bamfile)

    ### get pos for all reads
    pos_d = {}
    for read in samfile.fetch():
        pos_d[read.qname] = (read.reference_start, read.reference_end)

    ### pipeline:
    if args.mode=="end":
        end_d = count_end(pos_d)
    else:
        end_d=count_start(pos_d)

    end_d_f = filter_end(end_d, args.end_coverage)
    end_group_d = group_end(end_d_f, args.region_offset)
    ratio_d = scan_span_dic(pos_d, end_d_f, end_group_d)

    ## use py3 print to stdout
    for k in sorted(ratio_d.keys()):
        v = ratio_d[k]
        n_stop, n_span = v
        ratio = float(n_stop) / (n_stop + n_span)
        if ratio >= args.coverage_ratio:
            print("{}\t{}\t{}".format(k, n_stop, n_span))

    samfile.close()
