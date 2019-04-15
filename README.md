# flask-pluginkit-valine
Valine评论插件

### 安装

`pip install git+https://github.com/flask-pluginkit/flask-pluginkit-valine@master`

### 使用

- requirements.txt包含`git+https://github.com/flask-pluginkit/flask-pluginkit-valine@master`

- app.config配置：

    - PLUGINKIT_VALINE_APPID：必选，leancloud应用id

    - PLUGINKIT_VALINE_APPKEY：必选，leancloud应用key

    - PLUGINKIT_VALINE_PLACEHOLDER：可选，评论框中提示信息

    - 上述三项配置也可以不设置，转而放到配置文件中，会读取项目根目录下config.py中PLUGINS配置段（dict）下的Valine配置（dict），config.py示例：
        ```python
        PLUGINS = {
           "Valine": {
               "PLUGINKIT_VALINE_APPID": "xxx",
               "PLUGINKIT_VALINE_APPKEY": "xxx",
               "PLUGINKIT_VALINE_PLACEHOLDER": "xxx"
            }
        }
        ```

- 模板配置：

    - 在需要显示评论的地方引用：     `{{ emit_tep("valine_content") }}`

    - 在需要显示评论的页面js处引用： `{{ emit_tep("valine_script") }}`

### 示例

`python demo.py`
