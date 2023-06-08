# 使用 Python 3.8 作为基础镜像
FROM paddlepaddle/paddle:2.4.2

# 设置工作目录
WORKDIR /app

RUN pip install --upgrade paddlenlp && pip install --upgrade flask && pip install --upgrade waitress

# 将当前目录下的所有文件复制到工作目录
COPY . .

# 当容器启动时运行 Python 应用
CMD [ "python", "./main.py" ]