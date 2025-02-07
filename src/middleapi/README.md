# MiddleAPI

## 简介
MiddleAPI旨在不更改OpenWeb UI源代码的前提下，以一个中间人的身份将GPT-Sovits接入进OpenWeb UI TTS，并提供一个简单的WEB UI进行参数调节

## API总览
|  方法  |                 API                  |    功能     |
|:----:|:------------------------------------:|:---------:|
| GET  |        http://localhost:8000         |  Web UI   |
| POST |  http://localhost:8000/audio/speech  |   TTS推理   |
| POST | http://localhost:8000/app/getconfig  | TTS推理参数读取 |
| POST | http://localhost:8000/app/setconfig  | TTS推理参数设置 |

## API文档

### Web UI

#### 路径
| 方法  |          API          |   功能   | 请求体 |
|:---:|:---------------------:|:------:|:---:|
| GET | http://localhost:8000 | Web UI |  无  |

#### 请求体
| 参数 | 值 |
|:--:|:-:|
| 无  | 无 |

### TTS推理

#### 路径
|  方法  |                 API                 |   功能   | 请求体  |
|:----:|:-----------------------------------:|:------:|:----:|
| POST | http://localhost:8000/audio/speech | TTS推理 | JSON |

#### 请求体
|  参数   |  值   |
|:-----:|:----:|
| input | 输入文本 |
| voice | 目标语言 |

### TTS推理参数读取

#### 路径
|  方法  |                 API                 |   功能   | 请求体  |
|:----:|:-----------------------------------:|:------:|:----:|
| POST | http://localhost:8000/app/getconfig | TTS推理参数读取 | JSON |

#### 请求体
|   参数    |   值   |
|:-------:|:-----:|
| section | 配置节点名 |
|   key   |  配置名  |

### TTS推理参数设置

#### 路径
|  方法  |                 API                 |   功能   | 请求体  |
|:----:|:-----------------------------------:|:------:|:----:|
| POST | http://localhost:8000/app/setconfig | TTS推理参数设置 | JSON |

#### 请求体
|   参数    |   值   |
|:-------:|:-----:|
| section | 配置节点名 |
|   key   |  配置名  |
|  value  |  配置值  |

## 二次开发
1.克隆本项目
```bash
git clone git@github.com:TTTTTony32/GPTheresa.git
```
2.使用IDE打开本项目，推荐使用PyCharm或VS Code打开本项目