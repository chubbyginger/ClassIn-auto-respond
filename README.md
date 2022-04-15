# ClassIn-auto-respond
ClassIn自动抢答

## 介绍
自动识别屏幕上的抢答器的颜色，自动点击，用python编写

## 使用说明
先安装依赖库，然后windows如果关联了py launcher就可以直接双击打开。如果安装的是Anaconda，没有py launcher，就可以按住shift右键打开PowerShell，输入
```bash
conda activate base
python main.py
```

如果是macos或者Linux，请就地打开终端并输入
```bash
chmod +x main.py
```

使用前先将鼠标移动到扫描区域左上角、右下角处，然后用posLeftTop和posRightBot命令确定左上角、右下角坐标，然后把鼠标放在抢答器的按钮上，用getPixelData获取RGB信息，输入start即可自动识别抢答器，识别到了就会自动点击。

## 依赖库
pyautogui直接装最新版即可：
```bash
# 如果使用anaconda请加上这行
conda activate base

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui
```