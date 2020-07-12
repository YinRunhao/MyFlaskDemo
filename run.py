# -*- coding: utf-8 -*-
import DemoApp

# 创建应用
app = DemoApp.create_app()


def main():
    # 运行在2610端口上并接受所有地址的请求
    app.run(host='0.0.0.0', port=2610)


if __name__ == '__main__':
    main()
