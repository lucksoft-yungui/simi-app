# 使用 Python 3.8 作为基础镜像
FROM python:3.8.17-slim as paddle-nlp
# 设置工作目录
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pip 
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt


FROM paddle-nlp
# 将当前目录下的所有文件复制到工作目录
COPY . .
# 当容器启动时运行 Python 应用
CMD [ "python", "./main.py" ]