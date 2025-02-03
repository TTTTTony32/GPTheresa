# 使用官方 Python 3.11 Slim 作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行 FastAPI 应用，使用 Guvicorn 作为服务器
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "MiddleAPI:app"]