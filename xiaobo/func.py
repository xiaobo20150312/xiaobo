from blueking.component.shortcuts import get_client_by_user, get_client_by_request


def get_server_list(username, app_id):
    client = get_client_by_user(username)
    server_list_json = client.cc.get_app_host_list({'app_id': app_id})
    return server_list_json


def get_job_list(username, app_id):
    client = get_client_by_user(username)
    job_list_json = client.job.get_task({'app_id': app_id})
    return job_list_json


def get_app_list(username):
    client = get_client_by_user(username)
    app_list_json = client.cc.get_app_by_user()
    return app_list_json


def get_step_id(username, app_id, task_id):
    client = get_client_by_user(username)
    step_id = client.job.get_task_detail({'app_id': app_id, 'task_id': task_id})['data']['nmStepBeanList'][0]['stepId']
    return step_id


def execute_job(request, app_id, task_id, steps):
    client = get_client_by_request(request)
    execute_result = client.job.execute_task({'app_id': app_id, 'task_id': task_id, 'steps': steps})
    return execute_result
