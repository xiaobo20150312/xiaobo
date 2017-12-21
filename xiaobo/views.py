# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context
from func import get_app_list, get_job_list, get_server_list


def home(request):
    username = request.user.username
    app_list = []
    for app in get_app_list(username)['data']:
        app_id = app['ApplicationID']
        app_name = app['ApplicationName']
        job_list = get_job_list(username,app_id)['data']
        server_list= get_server_list(username,app_id)['data']
        app_dict = {'app_name': app_name, 'app_id': app_id, 'job_list': job_list, 'server_list': server_list}
        app_list.append(app_dict)
    app_list_dict = {'data': app_list}
    return render_mako_context(request, 'xiaobo/home.html', app_list_dict)
