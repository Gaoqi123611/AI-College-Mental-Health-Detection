# 基于AI大模型的大学生心理健康智能检测系统
本项目是面向大学生群体的心理健康智能筛查与情绪疏导系统，结合文本情绪识别、心理量表测评、风险预警与AI疏导，用于高校心理普查、辅导员预警、学生自我检测。

本项目为大学生创新创业大赛参赛项目，轻量化、可演示、可直接部署。

---

## 核心功能
1. 文本情绪分析：自动识别输入文本的情绪倾向，区分正常/轻度焦虑/中度抑郁/重度抑郁
2. 心理量表测评：支持SDS/SAS/SCL-90等常用心理量表，自动生成测评报告与风险分级
3. 心理风险预警：对高风险用户进行标记，辅助辅导员与心理咨询师及时介入
4. AI个性化疏导：针对不同心理状态生成专属情绪缓解建议与调节方案

---

## 技术栈
- 后端：Python + Flask
- 大模型：Qwen / ChatGLM 开源大模型
- 数据处理：Pandas、Numpy、Scikit-learn
- 前端：HTML + CSS + JavaScript

---

## 数据集说明
本项目采用公开数据集 + 自制数据集结合方式。

### 1. 公开数据集（dataset/public_dataset/）
- b_depressed.csv：抑郁标签数据集，用于模型基础训练
- clean_weibo_text.csv：微博中文抑郁情绪文本数据集

### 2. 自制数据集（dataset/self_build_dataset/）
- college_student_mental_self_build.csv
- 数量：200条
- 标签：正常 / 轻度焦虑 / 中度抑郁 / 重度抑郁
- 来源：大学生日常情绪仿写 + 模拟量表数据
- 特点：贴合校园场景，匿名合规

---

## 项目结构
AI-College-Mental-Health-Detection/
├── dataset/ # 数据集
│ ├── public_dataset/ # 公开数据集
│ └── self_build_dataset/ # 自制数据集
├── model/ # 模型代码
├── app/ # 网页 Demo
├── docs/ # 项目文档
└── README.md

## 快速运行（后续可直接使用）
```bash
git clone https://github.com/Gaoqi123611/AI-College-Mental-Health-Detection.git
cd AI-College-Mental-Health-Detection/model
pip install -r requirements.txt
cd ../app
python app.py
