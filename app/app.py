from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text', '')
    # 简单示例逻辑
    if '失眠' in text or '自卑' in text:
        result = "中度抑郁倾向，建议多和朋友沟通，必要时咨询专业老师"
    elif '压力大' in text or '焦虑' in text:
        result = "轻度焦虑倾向，建议适当放松，调整作息"
    else:
        result = "情绪状态良好，继续保持~"
    return render_template('index.html', text=text, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
