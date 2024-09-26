from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 假设的桌次信息，表明最低消费人数和最低消费金额
table_info = {
    1: {"min_people": 1, "min_spend": 150},
    2: {"min_people": 1, "min_spend": 150},
    3: {"min_people": 1, "min_spend": 150},
    4: {"min_people": 1, "min_spend": 150},
    5: {"min_people": 2, "min_spend": 300},
    6: {"min_people": 2, "min_spend": 300},
    7: {"min_people": 2, "min_spend": 300},
    8: {"min_people": 2, "min_spend": 300},
    9: {"min_people": 2, "min_spend": 300},
}


# 主页，显示餐厅平面图
@app.route('/')
def index():
    return render_template('index.html')

# 获取指定桌次的最低消费信息
@app.route('/table/<int:table_id>')
def get_table(table_id):
    info = table_info.get(table_id, {"min_people": 0, "min_spend": 0})
    return render_template('table.html', table_id=table_id, info=info)

# 顾客确认桌次信息后，可以进入点餐页面
@app.route('/confirm_table', methods=['POST'])
def confirm_table():
    data = request.json
    table_id = data['table_id']
    customer_id = data['customer_id']
    # 处理确认信息逻辑，例如保存订单或更新状态
    return jsonify({"status": "success", "message": f"Table {table_id} confirmed by customer {customer_id}"})

if __name__ == "__main__":
    app.run(debug=True)
