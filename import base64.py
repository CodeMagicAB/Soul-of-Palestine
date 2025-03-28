import base64
import os

def split_text(text, num_parts):
    part_size = len(text) // num_parts
    return [text[i * part_size: (i + 1) * part_size] for i in range(num_parts - 1)] + [text[(num_parts - 1) * part_size:]]

# قراءة الصورة وتحويلها إلى Base64
image_path = "4.jpg"
output_files = ["part1.txt", "part2.txt", "part3.txt", "part4.txt", "part5.txt", "part6.txt", "part7.txt", "part8.txt"]

with open(image_path, "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

# تقسيم النص إلى ثمانية أجزاء
split_parts = split_text(base64_string, len(output_files))

# حفظ كل جزء في ملف نصي منفصل
for file_name, content in zip(output_files, split_parts):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)

print("تم حفظ النص في 8 ملفات نصية.")
