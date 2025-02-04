![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/src/banner.jpg)
<div align="center">

# GPTheresa
**GPT-Theresa是基于LLM(大语言模型)与[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)的开源交互助理。**

想要了解更多，欢迎观看[视频](links_for_bilibili)介绍
</div>

## 特点


- **实现关联**: 
  - 本项目通过MiddleAPI.py实现GPT-SoVITS API接口与OpenWebUI API 接口的兼容。
  - 通过PRTS.py为LLM获取[PRTS wiki](https://prts.wiki)内容符合提供的世界观。
- **可调性强**:
  - 支持本地[Ollama](https://github.com/ollama/ollama)模型部署。
  - 支持[OpenAI API](https://openai.com/api/)接口的模型。
  - 支持GPT-SoVITS推理模型的参数传递。
- **安装简易**: 支持Docker部署以及手动部署。
## 实装模型
- **GPT-SoVITS**:特蕾西娅ckpt与pth推理模型。
- **LLM**:带有PRTS wiki检索功能的特蕾西娅LLM模型。

## 部署
### 通过Docker部署
### 手动部署
**手动部署时请严格按照给出步骤进行部署**

**1.安装OpenWebUI**

打开终端输入：
```bash
pip install open-webui
```

**2.准备LLM模型**

**2.1 本地模型**

- **2.1.1 安装[Ollama服务](https://ollama.com/download)**

- **2.1.2 选择本地模型:** 在[Ollama Library](https://ollama.com/library)中寻找适合的模型并在终端拉取

- 以deepseek-r1:7b为例:

- ```bash
  ollama run deepseek-r1:7b
  ```
- 下载完成后，出现如下视为成功：
- ```user
  >>> Send a message (/? for help)
  ```
- 现在已经可以进行对话：
  ```user
  >>> Who are you?
  ```
  ```deepseekr1:7b
  <think>

  </think>

  Greetings! I'm DeepSeek-R1, an artificial intelligence assistant created by DeepSeek. I'm at your service andwould be delighted to assist you with any inquiries or tasks you may have.
  ```
  - 退出对话:Ctrl+C

- **2.1.3 启动Ollama服务:**
  - 查看任务栏中Ollama是否已经启动。
  - 如果Ollama已启动,则无需输入任何命令。
  - 如果Ollama未启动，在终端输入:
    ```bash
      ollama serve
      ```
    出现调用GPU CUDA(测试电脑CUDA版本为12.6)信息视为成功:

    ```output
    time=202X-02-04TXX:XX:XX.XXX+XX:XX level=INFO source=types.go:131 msg="inference compute" id=GPU-12345678-abcd-efgh-ijkl-mnopqrstuiwx library=cuda variant=v12 compute=x.x driver=12.6 name="YOUR GPU" total="YOUR GPU GiB" available="X.X GiB"
    ```
  - **此时，Ollama服务已经默认监听本地11434端口**
- **Ollama 服务设置完成。**


**2.2 非本地模型**

- 2.2.1 请准备好**兼容OpenAI API接口的API url和API key**
- 2.2.2 在第六步内配置好非本地LLM API key。


**3.安装GPT-SoVITS**

- 3.1 以Windows压缩包为例，下载解压压缩包。 

- 3.2 进入目录双击 go-webui.bat。

- **3.3 此时GPT-SoVITS服务默认监听本地端口9874**

- 3.4 打开网页端，选择1-GPT-SoVITS-TTS下的1c推理，下拉找到”启动推理服务“并点击

- **3.5 此时GPT-SoVITS推理服务默认监听端口9872**

**GPT-SoVITS推理服务部署完成。**

**4.准备GPT-SoVITS模型**

*注意1：本文使用的是B站大佬Dear棉花糖的[【GPT-SoVITS】特雷西娅//魔王AI语音 模型分享/配布//附使用例](https://www.bilibili.com/video/BV1bH4y137Dn)*

- 4.1下载模型完成后，把下载好的模型覆盖到GPT-SoVITS目录。

*注意2：请记住小特.pth与小特.ckpt的路径*

- 4.2 **GPT-SoVITS模型部署完成**

**5.拉取PRTS.json和MiddleAPI.py**

- 5.1 在我们的文件中下载PRTS.json文件与MiddleAPI项目后，一并放入GPT-SoVITS目录下。
- 5.2 在终端输入
   ```bash
   pip install requirements.txt -r
   ```
- 5.3 完成下载后,双击run.bat启动MiddleAPI服务。出现如下则视为成功
   ```bash
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [XXXXXX] using StatReload
   INFO:     Started server process [XXXXXX]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```
- 5.4**此时MiddleAPI默认监听本地端口8000**

- **MiddleAPI设置成功**

**6.在OpenWebUI内配置模型**

- 6.1启动OpenWebUI

- ```bash
  open-webui serve
  ```
- 出现如下则视为启动成功
- ```output
  INFO:     Started server process [XXXX]
  INFO:     Waiting for application startup.
  INFO:     Application startup complete.
  INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
  ```
- **6.2 此时OpenWebUI默认监听本地端口8080**
- 6.3 打开OpenWebUI并创建自己的账号，登录。
- 6.4 选择**工作空间**>>**工具**>>**导入工具**>>选择PRTS.json，上传并刷新网页。
- 6.5 选择**工作空间**>>**模型**>>**导入模型**>>选择Theresa-AI-v3.json,上传并刷新网页,之后下拉,在**工具**一栏选择**PRTS**并保存设置.
- 6.6 选择**工作空间**>>**模型**>>**Theresa-AI-v3**下方的铅笔>>基础模型(来自)>>选择自己的LLM为基础模型,并在
  - 6.6.1 如果是本地模型,请确保Ollama服务已经开启;模型已经下载成功;**用户头像**>>**管理员面板**>>**设置**>>**外部链接**>>**Ollama API**的链接已开启并链接是本地端口11434.
  - 6.6.2 如果是非本地模型,请选择**用户头像**>>**管理员面板**>>**设置**>>**外部链接**>>**OpenAI API**>>**配置**,把自己的API URL,API key输入,后输入模型ID并点击加号,保存,并保存外部链接.
- 6.7 选择**用户头像**>>**管理员面板**>>**设置**>>**语音**>>**文本转语音设置**>>**文本转语音引擎**选择**OpenAI**,url输入" **https://localhost:8000** ",API key默认,**语音**输入**中文**,**文本转语音模型**默认.
- 6.8 **(可选)** 选择 **用户头像**>>**设置**>>**语音**>>**文本转语音设置**>>**自动念出回复内容**选择开启.
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
