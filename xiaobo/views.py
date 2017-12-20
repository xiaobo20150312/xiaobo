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
from blueking.component.shortcuts import get_client_by_request
from func import get_app_list, get_job_list, get_server_list


def home(request):
    username = request.user.username
    app_list = get_app_list(username)
    app_dict = {}
    for app in app_list:
        app_dict[app['ApplicationName']] = app['ApplicationID']
    return render_mako_context(request, 'xiaobo/home.html', app_dict)
