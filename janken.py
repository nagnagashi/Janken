# from flask import Flask, request, jsonify, render_template
# import random

# app = Flask(__name__)

# choices = ['グー', 'チョキ', 'パー']

# @app.route('/')
# def index():
#     return render_template('index.html')  # HTMLテンプレートを返す

# @app.route('/play', methods=['POST'])
# def play():
#     user_choice = request.json['choice']
#     cpu_choice = random.choice(choices)

#     # 勝敗判定
#     if user_choice == cpu_choice:
#         result = '引き分け'
#     elif (user_choice == 'グー' and cpu_choice == 'チョキ') or \
#          (user_choice == 'チョキ' and cpu_choice == 'パー') or \
#          (user_choice == 'パー' and cpu_choice == 'グー'):
#         result = 'あなたの勝ち！'
#     else:
#         result = 'あなたの負け！'

#     return jsonify({
#         'user_choice': user_choice,
#         'cpu_choice': cpu_choice,
#         'result': result
#     })

# if __name__ == '__main__':
#     app.run(debug=True)