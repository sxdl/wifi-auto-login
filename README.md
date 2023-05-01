# Wi-Fi Auto Login

华工校园网自动连接并登录，修改`module.mywifi.py`中的 request url 可以登录其他无线Wi-Fi portal.

# 快速开始
## 安装依赖
```shell
pip install -r requirements.txt
```

## 修改配置文件
复制`config-template.json`文件到同级目录下，并重命名为`config.json`.补充网络的 ssid，用户名和密码。

```json lines
{
  "ssid": "name of wifi",
  "user_account": "your account",
  "user_password": "your password"
}
```

## 运行项目代码
```shell
python main.py
```
