# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/4/24 12:34
# @Author    : 27
# @File    : csv_separate.py


# 读取第一行的n
import sys
from typing import List, Dict, Tuple


def build_letters_idx_map() -> Dict[str, int]:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_idx_map = {}
    idx = 0
    for char in letters:
        letters_idx_map[char] = idx
        idx += 1
    return letters_idx_map


def get_csv_input_line():
    csv_separated_line = sys.stdin.readline().strip().split(",")
    idx = 0
    for every_part_str in csv_separated_line:
        new_string = get_new_label_string(every_part_str, csv_separated_line)
        csv_separated_line[idx] = new_string
        idx += 1
    print(",".join(csv_separated_line))


def get_new_label_string(origin_string, origin_line_values):
    # 如果没有， 返回 False origin string
    # 最后一个参数返回需要替换为原始行那个位置的值
    is_labeled, format_string, target_letter = is_have_label(origin_string)
    if is_labeled:
        letter_map = build_letters_idx_map()
        target_index = letter_map[target_letter]
        replaced_value = origin_line_values[target_index]
        return format_string.format(replaced_value)
    return origin_string


def is_have_label(un_judge_str: str) -> Tuple[bool, str, str]:
    # 拿到诸如 <A>, 这种东西
    # 返回是否有这个label, 如果有，则返回可直接format的string
    # 比如 a<A>123， 返回a{}123
    stack = []
    left_str = ""
    right_str = ""
    idx = 0
    is_labeled = False
    target_letter = ""
    while idx < len(un_judge_str):
        curr_char = un_judge_str[idx]
        if curr_char == "<":
            stack.append(curr_char)
            try:
                stack.append(un_judge_str[idx + 1])
                target_letter = un_judge_str[idx + 1]
                last_sign = un_judge_str[idx + 2]
            except Exception as e:
                raise e
            else:
                if last_sign != ">":
                    raise Exception("invalid")
                else:
                    stack.append(last_sign)
            right_str = un_judge_str[idx + 3:]
            is_labeled = True
            break
        if not stack:
            left_str += curr_char
        else:
            break
        idx += 1
    return is_labeled, (left_str + "{}" + right_str), target_letter


if __name__ == '__main__':
    get_csv_input_line()

    pass