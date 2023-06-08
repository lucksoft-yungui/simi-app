import re


def remove_all_brackets_content(text):
    pattern = r'[\(（][^\)）]*[\)）]'
    replaced_text = re.sub(pattern, '', text)
    return replaced_text

# 示例用法
original_text = '规划意见书（规划函复）'
replaced_text = remove_all_brackets_content(original_text)
print(replaced_text)  # 输出: 规划意见书