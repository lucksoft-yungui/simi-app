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

# 测试
array1 = [('规划意见书', 'n')]
array2 = [('北京市', 'LOC'), ('丰台区', 'LOC'), ('中关村站', 'LOC'), ('规划意见书', 'n')]
target_types = ['n']

similarity = compute_similarity(array1, array2, target_types)
print(f"数组2与数组1的相似度为{similarity}%")