# -*- coding: utf-8 -*-
"""
    valine
    ~~~~~~

    A Comment System

    :copyright: (c) 2018 by Mr.tao.
    :license: BSD 3-Clause, see LICENSE for more details.
"""

#: Importing these two modules is the first and must be done.
#: 首先导入这两个必须模块
from __future__ import absolute_import
try:
    from config import PLUGINS
except ImportError:
    PLUGINS = {}
#: Import the other modules here, and if it's your own module, use the relative Import. eg: from .lib import Lib
#: 在这里导入其他模块, 如果有自定义包目录, 使用相对导入, 如: from .lib import Lib
from flask import g, current_app
#：Your plug-in name must be consistent with the plug-in directory name.
#：你的插件名称，必须和插件目录名称等保持一致.
__plugin_name__ = "Valine"
#: Plugin describes information. What does it do?
#: 插件描述信息,什么用处.
__description__ = "Valine是一款快速、简洁且高效的无后端评论系统"
#: Plugin Author
#: 插件作者
__author__      = "Mr.tao <staugur@saintic.com>"
#: Plugin Version
#: 插件版本
__version__     = "0.1.1"
#: Plugin Url
#: 插件主页
__url__         = "https://github.com/flask-pluginkit/flask-pluginkit-valine"
#: Plugin License
#: 插件许可证
__license__     = "BSD 3-Clause"
#: 插件状态, enabled、disabled, 默认enabled
__state__       = "enabled"


#: 返回插件主类
def getPluginClass():
    return ValineCommentApi

#: 插件主类, 不强制要求名称与插件名一致, 保证getPluginClass准确返回此类
class ValineCommentApi(object):

    def _set_app_info(self):
        """Valine需要LeanCloud应用的APP ID 和 APP Key，参考https://valine.js.org/quickstart.html"""
        g.valine_appId = current_app.config.get("PLUGINKIT_VALINE_APPID") or PLUGINS.get("Valine", {}).get("PLUGINKIT_VALINE_APPID")
        g.valine_appKey = current_app.config.get("PLUGINKIT_VALINE_APPKEY") or PLUGINS.get("Valine", {}).get("PLUGINKIT_VALINE_APPKEY")
        g.valine_placeholder = current_app.config.get("PLUGINKIT_VALINE_PLACEHOLDER") or PLUGINS.get("Valine", {}).get("PLUGINKIT_VALINE_PLACEHOLDER")

    def register_hep(self):
        return dict(before_request_hook=self._set_app_info)

    def register_tep(self):
        return {"valine_content": "valine/content.html", "valine_script": "valine/script.html"}
