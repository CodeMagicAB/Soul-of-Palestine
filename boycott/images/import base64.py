import base64

# قراءة الصورة وتحويلها إلى Base64
with open("12.jpeg", "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

# طباعة النص
print("'"+base64_string+"'")
