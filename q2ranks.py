def solution(ranks: list):
    """
    O(2n) => O(n)
    :param ranks: int list of ranks of soldiers
    :return:
    """
    count_reporting = 0
    rank_set = set()
    for rank in ranks:
        rank_set.add(rank)

    for rank in ranks:
        # leader check
        if rank + 1 in rank_set:
            count_reporting += 1

    return count_reporting
