<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-21 20:06:11
 * @FilePath: /xy_web_settings/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_web_settings

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

xy-web-service Service settings module.

## Source Code Repositories

| [Github](https://github.com/xy-web-service/xy_web_settings.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_settings.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_settings.git)          |
| ----------- | -------------|---------------------------------------|


## Installation

```bash
# bash
pip install xy_web_settings
```

## How to use

```python
# main.py
from xy_work.Settings.Section.Project import Project as xyProject
class Project(xyProject):
    def get_name(self) -> str | None:
        return "xy_web_project"

from xy_work.Settings.Section.Runner import Runner as xyWorkRunner

class Runner(xyWorkRunner):
    def get_name(self) -> str | None:
        return "xy_web_runner"

from pathlib import Path
from xy_web_settings.Settings import Settings as xySettings

class Settings(xySettings):
    project: Project | None
    runner: Runner | None

    def reload(self, settings_cfg_path: Path):
        super().reload(settings_cfg_path)
        self.project = self.make_section(Project)
        self.runner = self.make_section(Runner)

if __name__ == "__main__":
    settings = Settings()
    settings.reload(Path("./xy_web.toml"))
    print(f"project ===> {settings.project}")
    print(f"project.name ===> {settings.project.name}")
    print(f"project.identifier ===> {settings.project.identifier}")
```

```toml
# xy_web.toml
# ######################## xy_web_work配置 ###########################
# 默认配置文件位置为 当前工作目录下的 config/xy_web.toml

# ######################## xy_web_work项目配置 ###########################
[xy_web_project]

# 项目名称, 仅支持英文
name = "xy_web_demo"

# 项目标识
identifier = "d842087be5204c85a8bef764815348b5"

# 项目名称, 支持中英文
verbose_name = "xy-web-service Demo"

# 项目说明, 支持中英文
description = "xy-web-service Demo"

# 项目路径
path = "/home/helios/workspace/beachstudio/development/xy_web_demo"

# ######################## xy_web_work运行配置 ###########################

[xy_web_runner]

# 服务源码目录自动添加到sys.path 
# 默认 当前工作目录下的 source/Runner
path = "../source/Runner"

# 服务入口类，根据上文的path寻找对应的类初始化即为启动，字符串，若包含模块使用module.class根据importlib引入
# 默认 Runner.Runner
runner = "Runner.Runner"

```

```bash
# bash
python main.py
# project ===> {'path': '/home/helios/workspace/beachstudio/development/xy_web_demo', 'name': 'xy_web_demo', 'verbose_name': 'xy-web-service Demo', 'identifier': 'd842087be5204c85a8bef764815348b5', 'description': 'xy-web-service Demo'}
# project.name ===> xy_web_demo
# project.identifier ===> d842087be5204c85a8bef764815348b5
```

## License
xy_web_settings is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.


## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![pay-total](./pay-total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```