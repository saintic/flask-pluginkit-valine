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

- 模板配置：

    - 在需要显示评论的地方引用：     `{{ emit_tep("valine_content") }}`

    - 在需要显示评论的页面js处引用： `{{ emit_tep("valine_script") }}`

### 示例

`python demo.py`
