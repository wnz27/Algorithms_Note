# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/4/24 11:59
# @Author    : 27
# @File    : work_pipeline.py
"""
流水线
"""
import sys


# 工作是放进队列的， 先进先出，
# 流水线是循环从队列拿任务
# 三个流水线的最大值
from typing import Tuple


def get_pipeline_work_nums() -> Tuple[int, int]:
    # 拿到几个流水线， 几个任务
    pipeline, work_nums = sys.stdin.readline().strip().split()
    return int(pipeline), int(work_nums)


def get_cycle_list_next_idx(curr_idx, cycle_list: list) -> int:
    cl_length = len(cycle_list)
    next_idx = (curr_idx + 1) % cl_length
    return next_idx


def work_pipeline():
    pipeline_nums, work_nums = get_pipeline_work_nums()
    # 拿到所有作业时长
    work_queue = list(map(int, list(sys.stdin.readline().strip().split())))
    # 任务排序
    work_queue.sort()

    # 维护一个list 放每个流水线的任务
    pipelines = [0] * pipeline_nums
    pipeline_idx = 0
    while work_queue:
        curr_work_duration = work_queue.pop(0)
        pipelines[pipeline_idx] += curr_work_duration
        pipeline_idx = get_cycle_list_next_idx(pipeline_idx, pipelines)
    print(max(pipelines))


if __name__ == '__main__':
    work_pipeline()

    pass






