# MyFlaskDemo

这是一个基于Flask的小型Web API实例模板。默认使用2610端口

## 插件依赖

它依赖于以下插件：

|       插件名       |            用途             |
| :----------------: | :-------------------------: |
| flask_jwt_extended |         提供JWT验证         |
|      flasgger      | 提供Swagger的WebApi在线文档 |
|     flask_cors     |          CORS跨域           |
|  flask_sqlalchemy  |        数据库ORM框架        |
|      pymysql       |    MySQL Connector(可选)    |

> Windows下插件的安装脚本
```
pip install flask_jwt_extended
pip install flagsgger
pip install flask_cors
pip install flask_sqlalchemy
pip install pymysql
```

> Linux下插件安装脚本

```
pip3 install flask_jwt_extended
pip3 install flagsgger
pip3 install flask_cors
pip3 install flask_sqlalchemy
pip3 install pymysql
```

## 运行

运行总入口文件**run.py**即可

> python3 run.py

### 查看API在线文档

运行后用以下网访问API在线文档

> http://localhost:2610/apidocs

## 项目大致结构

```
    |-- run.py                             // 总入口
    |-- DemoApp                            // WebApi程序
        |-- controllers                    // Controller模块
            |-- DomoController.py
            |-- ...
            |-- __init__.py
        |-- models                        // 业务逻辑模块
            |-- db_models                 // 数据库实体类模块
            |-- dto_models                // 数据传输实体模块
            |-- ...
            |-- __init__.py
        |-- jwt                          // JWT插件模块
        |-- log                          // 日志模块
        |-- swagger                      // Swagger在线Api文档模块
        |-- config                       // 程序相关配置模块
        |-- __init__.py
```