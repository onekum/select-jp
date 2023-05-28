import re

# Read the file
with open('jp.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Replace non-Japanese characters with empty strings
clean_text = re.sub(r'[^\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\uFF00-\uFFEF\u4E00-\u9FAF]', '', text)

# Write the clean text back to the file
with open('jp.txt', 'w', encoding='utf-8') as file:
    file.write(clean_text)