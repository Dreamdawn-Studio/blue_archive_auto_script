# Blue Archive Auto Script
![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=python)

baas，一个带GUI的蔚蓝档案（全服支持），为屏幕分辨率为 16：9 (1280x720 最佳) 运行的场景而设计 最终目的是接管一切蔚蓝档案任务 实现完全自动化

baas 是一款免费开源软件，地址：https://github.com/pur1fying/blue_archive_auto_script

GUI support, thanks **[@キラメイ Kiramei](https://github.com/Kiramei)** 
感谢其他contributors

GUI预览图：
![gui](https://github.com/pur1fying/blue_archive_auto_script/blob/master/ui.png)
![gui](https://github.com/pur1fying/blue_archive_auto_script/blob/master/ui2.png)
![gui](https://github.com/pur1fying/blue_archive_auto_script/blob/master/ui3.png)
## 功能 Features
- **主线** 自动推图(普通4-23，困难1-23)其他图会陆续加入
- **咖啡厅** 邀请券可选择指定学生 咖啡厅摸头 咖啡厅奖励
- **商店** 支持指定普通物品商店 以及竞技场商店自动购买和刷新次数
- **收获**：每日小组体力 邮箱 竞技场每日领奖 总力战累计积分领奖 每日任务领奖
- **体力清理**：可指定任意主线关卡(普通困难) 特别委托 扫荡任意次数
- **日程** 指定每个区域日程次数
- **竞技场** 清理到没有竞技场挑战券为止，自动领取每日奖励
- **制造** 可选择制造物品优先级 制造次数 (可选择是否使用加速券)
- **momo_talk** 自动完成所有未结束对话 完成剧情 领取青辉石
- **总力战** 清空总力战挑战券并领取奖励(auto)
- **剧情** 一键清理主线剧情，小组剧情

#### 突出特性：

- **16:9分辨率模拟器都可以运行，不局限于1280x720**
- **在低配电脑上运行也不会出现问题** 处理器速度低的电脑可以手动调小截图速度 增长运行时间

## 安装 Installation 
  **请确保安装路径没有中文(QT框架限制)**
  解压Release或qq交流群中的下载包，双击`BlueArchiveAutoScript.exe`安装环境，请耐心等待。
  安装完成后，BAAS 的ui界面将自动启动。

## 如何使用
一些关键的参数
- **模拟器最佳是16：9尺寸**
- **服务器：官服/b服/国际服/日服**
- **连接安卓模拟器：请设置端口号(模拟器多开请自行查询对应端口号)**
- **截图间隔：0.3s (CPU性能高)  /  0.5s - 2s(CPU性能较低)**
  **国际服必须使用英文语言**
## 如何上报bug How to Report Bugs
在提问题之前至少花费 5 分钟来思考和准备，才会有人花费他的 5 分钟来帮助你。

在提问题前，请先。
检查 BAAS 的更新，确认使用的是最新版。
如果是非预期的行为，请提供非预期行为发生时UI界面的日志,模拟器截图或视频。

## 已知问题 Known Issues

- **ocr中文文字识别精度尚可,但不是特别高**
- **截图速度过快可能导致问题**

## 联系我们 Contact Us

- QQ群：658302636 （有开发意向请加作者 Email pur1fying at 2274916027@qq.com）

## 未来目标 Future Goals
- **学生党，痛苦喵，大家一起来开源喵**
- **完善异常检测机制**
- **训练一个高精度ocr模型**
