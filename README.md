![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/pics/en/banner_en.png)
<div align="center">

# GPTheresa
**GPT-Theresa is an open-source interactive assistant based on LLM (Large Language Model) and [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS).**

**English** | [**中文简体**](./docs/cn/README.md)

---
For more information, feel free to watch the [video](links_for_bilibili) introduction.
</div>

## Features
- **Role-Playing**:
  - This project is dedicated to using open-source models and frameworks to deploy a private chat assistant locally through Prompt Engineering, allowing the LLM to play a specific role.
- **Expandable Interfaces**: 
  - The`GPT-SoVITS` TTS service is made compatible with the `OpenWebUI` TTS interface through a middleware API.
  - The `tools` feature of `OpenWebUI` enables the LLM to access the content of the [PRTS wiki](https://prts.wiki). Combined with the model's `Function Calling` feature, this allows for automatic content retrieval, reducing model hallucinations.
- **Adjustable Parameters**:
  - Supports advanced inference parameter adjustments for the `GPT-SoVITS` framework.
- **Flexible Deployment**:
  - Supports local [Ollama](https://github.com/ollama/ollama) model deployment.
  - Supports online models(must support the [OpenAI API](https://openai.com/api/) format).
- **Easy Installation**:
  - Supports one-click deployment with Docker Compose.
  - Provides manual deployment steps for advanced users.

## Implemented Models
This project provides some pre-optimized models that are ready to use out of the box.
- **Theresa**:The base model is `Qwen-2.5`, which includes system prompts, the GPT-SoVITS model, and the ability to access PRTS.

## Performance Requirements
The table below shows the performance of some open-source models supported by Ollama in this project.

Test platform:

NVIDIA RTX 4090 24G

Intel Xeon Platinum 8352V

120G RAM

| Model                        | Full Prompt | PRTS | Realization Effect* |
| :---------------------------: | :----------: | :----: | :--------: |
| Qwen2.5:0.5B                | ✅          | ❌    | 15%      |
| Qwen2.5:1.5B                | ✅          | ⛔    | 20%      |
| **Qwen2.5:7B**                  | ✅          | ⛔    | **45%**      |
| **Qwen2.4:14B**                 | ✅          | ✅    | **70%**      |
| GLM4:9B                     | ✅          | ✅    | 40%      |
| DeepSeek-R1:1.5B            | ✅          | ❌    | 20%      |
| DeepSeek-R1:7B              | ✅          | ❌    | 20%      |
| deepseek-r1-tool-calling:7B | ✅          | ✅    | 30%      |

Based on the information in the table, we recommend that users deploy locally with models of at least `Qwen2.5:7B` or larger to achieve the best results.

In terms of PC configuration, we recommend using at least an RTX 30 series graphics card with >8G of video memory; otherwise, you may not be able to deploy and use this project smoothly.

***Note: The sample size for the realization effect is too small, so it does not have significant reference value.**

**For users with limited PC performance, please use API to access large models and skip the GPT-SoVITS deployment.**

## Deployment

The schematic diagram of this project is as follows:

![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/pics/en/main_structure_en.png)
  
###  Docker Deployment
  Since this project integrates two large open-source projects, `OpenWebUI` and `GPT-SoVITS`, he manual deployment steps are quite cumbersome. After deployment, several terminals need to be started, which is not conducive to long-term use. Therefore, we strongly recommend users to deploy our project using Docker.
  > ⚠️Note
  > 
  > Before starting, please confirm that your device has Docker installed.
  > 
  > Windows users should install WSL2 and Docker Desktop.
  > 
  > You can refer to [this link](https://docs.docker.com/desktop/setup/install/windows-install/) for installation.
  
  Clone this project or directly download the zip file
  ```bash
  git clone https://github.com/TTTTTony32/GPTheresa.git
  ```
  Enter the `src` directory, select the appropriate deployment command from the table below based on your needs, and deploy using Docker Compose:

  | Deployment Package Introduction                               |   Command |
  | :--------------------------------: |  :------------------------------------------------: |
  | Online model API + GPT-SoVITS CPU inference          | `docker compose -f .\docker-compose-cpu.yml up --build -d`  |      
  | **Online model API + GPT-SoVITS GPU inference**          | `docker compose -f .\docker-compose-gpu.yml up --build -d`  |       
  | Local model + GPT-SoVITS CPU inference          | `docker compose -f .\docker-compose-local-cpu.yml up --build -d` |         
  | Local model + GPT-SoVITS GPU inference          | `docker compose -f .\docker-compose-local-gpu.yml up --build -d` |       

If you choose to use the **Online model API + GPT-SoVITS GPU inference**, enter the following command in the terminal:
  ```bash
  docker compose -f .\docker-compose-gpu.yml up --build -d
  ```
  After completion, you can connect to the port opened by the Docker container to enter OpenWebUI and start using it (default is `8080`).
### Manual Deployment
#### Windows Users
1. **Install OpenWebUI**

    Open the terminal and enter:
    ```bash
    pip install open-webui
    ```
2. **Prepare the LLM Model**
    1. **If you plan to deploy the model locally:**

       Install[Ollama](https://ollama.com/download).
       
       Deploy the local model: Find a suitable model in the [Ollama Library](https://ollama.com/library)and pull it in the terminal.
       
       > ⚠️Note
       > 
       > Please choose a model that supports the `Function Calling` feature, otherwise, you may encounter**无法搜索PRTS** (*translation:unable to search PRTS.*)
       > 
       > As a reference, you can check [this link](https://docs.siliconflow.cn/guides/function-calling#3) for a list of open-source models that support Function Calling.
       > 
       > `DeepSeek-R1` does not support the Function Calling feature. Users with this requirement should use the `DeepSeek-V3` or `Qwen-2.5-7B-Instruct` model.

       Taking `deepseek-r1:7b` as an example:
       ```bash
       ollama run deepseek-r1:7b
       ```
       After the download is complete, the following message indicates success:
       ```user
       >>>Send a message (/? for help)
       ```
       Check if Ollama is running in the taskbar. If Ollama is already running, no further commands are needed. If Ollama is not running, enter in the terminal:
       ```bash
       ollama serve
       ```
       The appearance of GPU CUDA information indicates success (the CUDA version of the test computer is 12.6):
       ```output
       time=202X-02-04TXX:XX:XX.XXX+XX:XX level=INFO source=types.go:131 msg="inference compute" id=GPU-12345678-abcd-efgh-ijkl-mnopqrstuiwx library=cuda variant=v12 compute=x.x driver=12.6 name="YOUR GPU" total="YOUR GPU GiB" available="X.X GiB"
       ```
       At this point, the Ollama service is listening on the local port `11434`.

    2. **If you plan to use an API**

       Please check whether your model provider offers an API interface compatible with the `OpenAI API` format.
       > The DeepSeek API is already compatible with the OpenAI API.
       > 
       > Most intermediary service providers offer the OpenAI API interface.

3. **Install GPT-SoVITS**

    Download and extract the zip file.

    Download the [start_inference.bat](https://github.com/TTTTTony32/GPTheresa/blob/main/src/start_inference.bat)  from our `src` directory.

    Place `start_inference.bat`  into the root directory of GPT-SoVITS.

    Double-click to open.

    At this point, the GPT-SoVITS inference service is listening on the local port `9872` by default

4. **Prepare the GPT-SoVITS Model**

    > This article uses the model from this brilliant Bilibili user [Dear棉花糖's Model](https://www.bilibili.com/video/BV1bH4y137Dn).

    Copy the downloaded model to the `GPT-SoVITS` directly.

    > ⚠️Note
    >
    > Please remember the paths of `小特.pth` and `小特.ckpt`.

5. **Download the PRTS Toolkit and MiddleAPI**

  Clone this project or directly download the zip file:
    ```bash
    git clone https://github.com/TTTTTony32/GPTheresa.git
    ```
    Enter the `src` folder and copy the `MiddleAPI` folder and `prts.json` file to the GPT-SoVITS path.

    Enter the `MiddleAPI` directory and enter in the terminal:
    ```bash
    pip install requirements.txt -r
    ```
    After the download is complete, double-click `run.bat` to start the MiddleAPI service. The following message indicates success.
    ```bash
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [XXXXXX] using StatReload
    INFO:     Started server process [XXXXXX]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```
   At this point, MiddleAPI is listening on the local port `8000` by default.

6. **Configure the Model in OpenWebUI**

   Start OpenWebUI:
    ```bash
    open-webui serve
    ```
    The following message indicates successful startup:
    ```output
    INFO:     Started server process [XXXX]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
    ```
    At this point, OpenWebUI is listening on the local port `8080` by default.
    Open `https://localhost:8080` to enter OpenWebUI
    - **If you choose local deployment**

        Ensure that the Ollama service is running and the model has been downloaded.

        Click **User Avatar**>>**Admin Panel**>>**Settings**>>**External Links**>>Confirm that **Ollama API** is enabled, withe the default port `11434`
    
    - **If you choose to use an online API**

        Click **User Avatar**>>**Admin Panel**>>**Settings**>>**External Links**>>**OpenAI API**>>**Configuration**

        Enter the `API URL` and `API key`, input the model ID in the field below and click the plus sign to save.

        > ⚠️Note
        >
        > The model ID is the ID that OpenWebUI requests from the API provider when requesting the model. Please make sure to fill it in completely and correctly.

    Select **Workspace**>>**Tools**>>**Import Tool**>>Import PRTS.json, upload and refresh the webpage.
   
    Select **Workspace**>>**Models**>>**Import Model**>>Import Theresa-AI-v3.json, upload and refresh the webpage.
   
    Select the edit button below**Theresa-AI-v3** in **Workspace**>>**Models**,choose your own LLM as the base model, and select **PRTS** in the **Tools** section, then save the settings.
   
    Select **User Avatar**>>**Admin Panel**>>**Settings**>>**Voice**>>**TTS Settings**>>**TTS Engine** and choose **OpenAI**, configuring it as follows:
    ```
    URL: https://localhost:8000
    API key: Default
    Voice: 中文
    TTS model: Default
    ```
   
    **(Optional)** Select  **User Avatar**>>**Settings**>>**Voice**>>**TTS Settings**>>**Automatically Read Out Replies**.

### **Congratulations, you have completed the installation and can start chatting!**

## Future Plans
- Support more roles.
- Support more voice tones.
- Simplify deployment.
## Credits
- [OpenWebUI](https://github.com/open-webui/open-webui)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [Ollama](https://github.com/ollama/ollama)
- [PRTS wiki](https://prts.wiki)
- Voice model provider [Dear棉花糖](https://space.bilibili.com/7044180)

## License
- [BSD-V3](https://github.com/TTTTTony32/GPTheresa/blob/main/LICENSE)
## Support

Feel free to join our qq group(146052965), or scan the QR code below:

![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/pics/qr/qr-qq.png)

## Sponsor

We thank all of our supporters and if you would like to buy us a cup of coffee, you can scan the QR code below:

![](https://raw.githubusercontent.com/TTTTTony32/GPTheresa/main/pics/qr/qr-support.png)

## The Project is created by **[Tony32](https://github.com/TTTTTony32)** **[NekokeCore](https://github.com/NekokeCore)** **[DeckDes](https://github.com/DeckDes233)**
