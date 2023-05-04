# Wi-Fi Auto Login

华工校园网自动连接并登录，修改`module.mywifi.py`中的 request url 可以登录其他无线Wi-Fi portal.

# 快速开始
## 安装依赖
```shell
pip install -r requirements.txt
```

## 修改配置文件
复制`config-template.json`文件到同级目录下，并重命名为`config.json`. 根据需要更改网络的 ssid，请求url和浏览器headers。

请求url和浏览器headers的获取：浏览器打开到 Wi-Fi 登录界面，F12 进入调试模式抓包。先进入`网络`选项，再登录认证，点击第一个Get包查看url和请求headers。

```json lines
{
  "ssid": "",
  "url": "",
  "headers": {
    "Host": "",
    "Referer": "",
    "User-Agent": ""
  }
}
```

## 运行项目代码
```shell
python main.py
```
