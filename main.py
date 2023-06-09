from paddlenlp import Taskflow
import re
from flask import Flask, request, jsonify

SERVICE_IP = "0.0.0.0"
SERVICE_PORT = 8686

tag = Taskflow("pos_tagging", user_dict="user_dict.txt")
target_types = ['n']


def simi(var1: str, var2: str) -> dict:
    s1 = remove_all_brackets_content(var1)
    s2 = remove_all_brackets_content(var2)

    tag1 = tag(s1)
    tag2 = tag(s2)

    print(tag1)
    print(tag2)

    similarity = compute_similarity(tag1, tag2, target_types)
    return {"result": f"句子[{var1}]与句子[{var2}]的相似度为{similarity}%", "tag1": f"{tag1}", "tag2": f"{tag2}"}


def compute_similarity(array1, array2, target_types=['n']):
    # 找出指定类型的词
    words1 = {word for word, type in array1 if type in target_types}
    words2 = {word for word, type in array2 if type in target_types}

    # 计算完全匹配的情况
    if words1 == words2:
        return 100

    # 计算不匹配度
    all_words = words1.union(words2)
    mismatched_words = all_words - words1.intersection(words2)
    mismatch_ratio = len(mismatched_words) / len(all_words)

    # 计算相似度
    similarity = 1 - mismatch_ratio
    return similarity * 100


def remove_all_brackets_content(text):
    pattern = r'[\(（][^\)）]*[\)）]'
    replaced_text = re.sub(pattern, '', text)
    return replaced_text


app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/simi', methods=['GET'])
def get_books():
    var1 = request.args.get('var1')
    var2 = request.args.get('var2')

    return jsonify(simi(var1, var2))


if __name__ == '__main__':
    print("start server……")
    from waitress import serve
    serve(app, host=SERVICE_IP, port=SERVICE_PORT)
    print("server stopped……")
