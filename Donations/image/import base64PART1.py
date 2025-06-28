import base64
import os

# مسار الصورة
image_path = "image/Egypt.png"
output_file = "image_base64.txt"

# التأكد إن الصورة موجودة
if not os.path.exists(image_path):
    print(f"❌ الملف غير موجود: {image_path}")
    exit()

# قراءة الصورة وتحويلها إلى Base64
with open(image_path, "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

# حفظ النص في ملف واحد
with open(output_file, "w", encoding="utf-8") as file:
    file.write(base64_string)

print("✅ تم حفظ الصورة بصيغة Base64 في ملف واحد.")
