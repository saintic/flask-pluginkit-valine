from flask import Flask, render_template_string
from flask_pluginkit import PluginManager

app = Flask(__name__)
app.config.update(
    PLUGINKIT_VALINE_APPID="g4pC9ql0dNcmeAhouAzS934z-gzGzoHsz",
    PLUGINKIT_VALINE_APPKEY="o43q3v8xQfpfatvQPbaATJKV"
)
plugin = PluginManager(app, plugin_packages=["flask_pluginkit_valine"])

@app.route("/test")
def test():
    return "test"

@app.route("/")
def index():
    return render_template_string("""
<html>
    <head>
    </head>
    <body>
        {{ emit_tep("valine_content") }}
        {{ emit_tep("valine_script") }}
    </body>
</html>
""")

if __name__ == "__main__":
    app.run(debug=True)
