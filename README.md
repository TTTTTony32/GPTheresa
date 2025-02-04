![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/src/banner.jpg)
<div align="center">

# GPTheresa
**GPT-Theresa是基于LLM(大语言模型)与[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)的开源交互助理。**

想要了解更多，欢迎观看[视频](links_for_bilibili)介绍
</div>

## 特点
- **角色扮演**：
  - 本项目致力于使用开源模型和框架，通过Prompt Engeneering实现本地部署私人聊天助理，并让LLM扮演特定角色。
- **拓展接口**: 
  - 通过中间API将`GPT-SoVITS`TTS服务与`OpenWebUI`TTS接口兼容。
  - 通过`OpenWebUI`的`tools`功能，使得LLM能够获取[PRTS wiki](https://prts.wiki)内容，结合模型的`Function Calling`特性，实现自动检索内容，减少模型幻觉。
- **参数可调**：
  - 支持`GPT-SoVITS`框架的高级推理参数调整。
- **弹性部署**：
  - 支持本地[Ollama](https://github.com/ollama/ollama)模型部署。
  - 支持在线模型（需支持[OpenAI API](https://openai.com/api/)格式）。
- **安装简易**:
  - 支持Docker Compose一键部署。
  - 对于高级用户，提供手动部署步骤。

## 实装模型
本项目内部提供部分已调优的模型，可开箱即用
- **特蕾西娅**：基础模型`Qwen-2.5`，包含系统提示词、GPT-SoVITS模型、PRTS接入能力。

## 部署

本项目的示意图如下:

![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/src/main_structure.png)
  
### 通过Docker部署
### 手动部署
#### Windows用户
1. **安装OpenWebUI**

    打开终端输入：
    ```bash
    pip install open-webui
    ```
2. **准备LLM模型**
    1. **若您计划本地部署模型：**

       安装[Ollama](https://ollama.com/download)
       
       部署本地模型：在[Ollama Library](https://ollama.com/library)中寻找适合的模型并在终端拉取
       
       > ⚠️注意
       > 
       > 请选择支持`Function Calling`特性的模型，否则可能会出现无法搜索PRTS的情况
       
       以deepseek-r1:7b为例：
       ```bash
       ollama run deepseek-r1:7b
       ```
       下载完成后，出现如下视为成功：
       ```user
       Send a message (/? for help)
       ```
       查看任务栏中Ollama是否已经启动，如果Ollama已启动,则无需输入任何命令，如果Ollama未启动，则在终端输入:
       ```bash
       ollama serve
       ```
       出现调用GPU CUDA信息视为成功（测试电脑CUDA版本为12.6）：
       ```output
       time=202X-02-04TXX:XX:XX.XXX+XX:XX level=INFO source=types.go:131 msg="inference compute" id=GPU-12345678-abcd-efgh-ijkl-mnopqrstuiwx library=cuda variant=v12 compute=x.x driver=12.6 name="YOUR GPU" total="YOUR GPU GiB" available="X.X GiB"
       ```
       此时，Ollama服务监听本地端口`11434`

    2. **若您计划使用API：**

       请检查您的模型提供商是否提供兼容`OpenAI API`格式的API接口
       > DeepSeek API已经兼容OpenAI API
       > 
       > 大部分中转服务提供商均提供OpenAI API接口

3. **安装GPT-SoVITS**

    下载解压压缩包。 

    下载我们src目录下的 [start_inference.bat](https://github.com/TTTTTony32/GPTheresa/blob/main/src/start_inference.bat)

    将'start_inference.bat'放入GPT-SoVITS根目录

    双击打开。

    此时GPT-SoVITS推理服务默认监听本地端口`9872`

4. **准备GPT-SoVITS模型**

    > 本文使用的是B站大佬[Dear棉花糖的模型](https://www.bilibili.com/video/BV1bH4y137Dn)

    将下载好的模型覆盖到`GPT-SoVITS`目录

    > ⚠️注意
    >
    > 请记住小特.pth与小特.ckpt的路径

5. **下载PRTS工具包和MiddleAPI**

    克隆本项目或直接下载压缩包
    ```
    git clone https://github.com/TTTTTony32/GPTheresa.git
    ```
    进入`src`文件夹，将`MiddleAPI`文件夹与`prts.json`文件复制到GPT-SoVITS路径下

    进入`MiddleAPI`路径，在终端输入
    ```bash
    pip install requirements.txt -r
    ```
    完成下载后,双击`run.bat`启动MiddleAPI服务，出现如下提示视为成功
    ```bash
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [XXXXXX] using StatReload
    INFO:     Started server process [XXXXXX]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```
    此时MiddleAPI默认监听本地端口`8000`

6. **在OpenWebUI内配置模型**

    启动OpenWebUI
    ```bash
    open-webui serve
    ```
    出现如下则视为启动成功
    ```output
    INFO:     Started server process [XXXX]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
    ```
    此时OpenWebUI默认监听本地端口`8080`
    打开`https://localhost:8080`进入OpenWebUI
    - **如果您选择本地部署**

        请确保Ollama服务已经开启且已经下载模型

        点击**用户头像**>>**管理员面板**>>**设置**>>**外部链接**>>确认**Ollama API**为启用状态，默认端口`11434`
    
    - **如果您选择使用在线API**

        点击**用户头像**>>**管理员面板**>>**设置**>>**外部链接**>>**OpenAI API**>>**配置**

        输入`API URL`和`API key`，在下方输入模型ID并点击加号，保存

        > ⚠️注意
        >
        > 模型ID为OpenWebUI向API提供商请求模型时的ID，请务必填写完整、正确

    选择**工作空间**>>**工具**>>**导入工具**>>导入PRTS.json，上传并刷新网页
   
    选择**工作空间**>>**模型**>>**导入模型**>>导入Theresa-AI-v3.json，上传并刷新网页
   
    选择**工作空间**>>**模型**>>**Theresa-AI-v3**下方的编辑按钮>>基础模型(来自)>>选择自己的LLM为基础模型，并在**工具**一栏选择**PRTS**并保存设置
   
    选择**用户头像**>>**管理员面板**>>**设置**>>**语音**>>**文本转语音设置**>>**文本转语音引擎**选择**OpenAI**，并按如下内容配置：
    ```
    URL: https://localhost:8000
    API key: 默认
    语音: 中文
    文本转语音模型: 默认
    ```
   
    **(可选)** 选择 **用户头像**>>**设置**>>**语音**>>**文本转语音设置**>>**自动念出回复内容**

### **恭喜,您完成了安装,可以去聊天了!**

## 未来计划
- 支持更多角色。
- 支持更多音色。
- 简化部署
## 致谢
- [OpenWebUI](https://github.com/open-webui/open-webui)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [Ollama](https://github.com/ollama/ollama)
- [PRTS wiki](https://prts.wiki)
- 音色模型提供者 [Dear棉花糖](https://space.bilibili.com/7044180)

## 协议
- BSDV3[]
## 支持
## 赞助
