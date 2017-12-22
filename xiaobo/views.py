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
from func import *
from django.http import HttpResponse
import json


def home(request):
    username = request.user.username
    app_id = request.GET.get('app_id', 3)
    return_list = get_server_list(username, app_id)
    return render_mako_context(request, 'xiaobo/home.html', return_list)


def do_job(request):
    username = request.user.username
    step_id = get_step_id(username, 3, 13)
    ip = request.GET.get('host_ip')
    iplists = '1' + ':' + ip
    steps = [{'stepId': step_id, 'ipList': iplists}]
    result_dict = execute_job(request, 3, 13, steps)
    result_json = json.dumps(result_dict)

    return HttpResponse(result_json)
