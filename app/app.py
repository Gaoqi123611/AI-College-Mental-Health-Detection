from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# 加载数据集（仅用于示例）
df = pd.read_csv('../dataset/self_build_dataset/college_student_mental_self_build.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text', '')
    # 这里是简单的示例逻辑，后续可以接入大模型
    if '失眠' in text or '自卑' in text:
        result = "中度抑郁倾向，建议多和朋友沟通，必要时咨询专业老师"
    elif '压力大' in text or '焦虑' in text:
        result = "轻度焦虑倾向，建议适当放松，调整作息"
    else:
        result = "情绪状态良好，继续保持~"
    return render_template('index.html', text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)
