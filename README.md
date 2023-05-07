# Wi-Fi Auto Login

华工校园网自动连接并登录，修改`module.mywifi.py`中的 request url 可以登录其他无线Wi-Fi portal.

# 快速开始
## 克隆代码仓库
```shell
git clone https://github.com/sxdl/wifi-auto-login.git
```
```shell
cd wifi-auto-login
```

## 安装依赖

```shell
pip install -r requirements.txt
```

## 修改配置文件
复制`config-template.json`文件到同级目录下，并重命名为`config.json`. 根据需要更改网络的 ssid，请求url和浏览器headers。

请求url和浏览器headers的获取：浏览器打开到 Wi-Fi 登录界面，F12 进入调试模式抓包。先进入`网络`选项，再登录认证，点击第一个Get包查看url和请求headers。

```json lines
{
  "ssid": "scut-student",            // Wi-Fi名称
  "auto_ip": "wlan_user_ip",         // 自动填充ip的参数名，默认为空
  "request":
  {
    "url": "https://s2.scut.edu.cn:801/eportal/",
    "params":                        // 根据实际情况修改请求参数
    {
      "c": "Portal",
      "a": "login",
      "callback": "dr1003",
      "login_method": "1",
      "user_account": ",0,",         // 用户名，加上“,0,”前缀
      "user_password": "",           // 密码，需要填充
      "wlan_user_ip": "",            // 局域网 ip 地址
      "wlan_user_ipv6": "",          // ipv6 ip 地址，没有为空
      "wlan_user_mac": "000000000000",
      "wlan_ac_ip": "xxx.xx.xx.xx",  // ac ip，需要抓包查看
      "wlan_ac_name": "AC",
      "jsVersion": "3.3.2"
    },
    "headers":
    {
      "Host": "s2.scut.edu.cn:801",
      "Referer": "https://s2.scut.edu.cn/",
      "User-Agent": ""               // 浏览器 User-Agent，需要填写
    }
  }
}
```

## 运行项目代码
```shell
python main.py
```
