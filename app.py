from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# هتحملي القرآن من ملف JSON ونحطه هنا
with open('quran.json', 'r', encoding='utf-8') as f:
    quran_data = json.load(f)

# ده مسار بيجيب كل القرآن
@app.route('/')
def home():
    return "السلام عليكم! API المصحف الشريف شغال ✅"

# ده المسار اللي هتجيب بيه الصفحة
@app.route('/page/<int:page_number>')
def get_page(page_number):
    if 1 <= page_number <= 604:
        page_key = str(page_number)
        if page_key in quran_data:
            return jsonify({
                'page': page_number,
                'verses': quran_data[page_key]
            })
    return jsonify({'error': 'الصفحة غير موجودة'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)