from flask import Flask
app = Flask(__name__)
app.debug=False

# 导入app1/views.py中创建的蓝图
from train_mock.urls import train_bp
from hotel_mock.views import hotel_bp
# 注册该蓝图
app.register_blueprint(train_bp)
app.register_blueprint(hotel_bp)