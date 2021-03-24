def solution(blocks: list):
    """

    :param blocks: int list of block heights. 0-indexed
    :return:
    """

    # [i] = max jump to the left/right for the i-th spot
    num_blocks = len(blocks)
    max_left_jump = fill_list([], 0, num_blocks)
    max_right_jump = fill_list([], 0, num_blocks)

    # calculate left jumps for every block
    for i in range(1, len(blocks)):
        if blocks[i - 1] < blocks[i]:
            max_left_jump[i] = 0
        else:
            max_left_jump[i] = max_left_jump[i - 1] + 1

    # calculate right jumps for every block
    for i in range(len(blocks) - 2, -1, -1):
        if blocks[i + 1] < blocks[i]:
            max_right_jump[i] = 0
        else:
            max_right_jump[i] = max_right_jump[i + 1] + 1

    # try every block spot
    best_answer = 0
    for i in range(len(blocks)):
        answer = max_left_jump[i] + max_right_jump[i]

        # frog distance is calculated weirdly.
        if answer != 0:
            answer += 1

        if answer > best_answer:
            best_answer = answer

    return best_answer


def fill_list(the_list: list, number: int, size: int):
    """
    fill the_list with numbers up until the size.
    :param the_list: the list to alter
    :param number: the number to fill the list with
    :param size:
    :return:
    """
    for i in range(size):
        the_list.append(number)

    return the_list
