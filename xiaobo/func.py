from blueking.component.shortcuts import get_client_by_user


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
