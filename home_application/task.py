# -*- coding: utf-8 -*-

from blueking.component.shortcuts import get_client_by_user


def test1(n):
    username = 'admin'
    client = get_client_by_user(username)
    result = client.cc.get_app_host_list({'app_id': n})

    return result


def execute():
    username = 'public'
    client = get_client_by_user(username)
    result = client.job.execute_task({'app_id': 3, 'task_id': 13})

    return result


def get_result():
    username = 'public'
    client = get_client_by_user(username)
    result = client.job.get_task_detail({'app_id': 3, 'task_id': 13})
    return result


def xiaobo():
    username = 'admin'
    client = get_client_by_user(username)
    result = client.xiaobo.test1()
    return result
