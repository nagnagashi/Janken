from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

choices = ['グー', 'チョキ', 'パー']

# 勝率計算用の変数
win_count = 0
lose_count = 0
draw_count = 0
total_games = 0


@app.route('/')
def index():
    return render_template('index.html')  # HTMLテンプレートを返す

@app.route('/play', methods=['POST'])
def play():
    global win_count, lose_count, draw_count, total_games
    user_choice = request.json['choice']
    cpu_choice = random.choice(choices)

    # 勝敗判定
    if user_choice == cpu_choice:
        result = '引き分け'
        draw_count += 1
    elif (user_choice == 'グー' and cpu_choice == 'チョキ') or \
         (user_choice == 'チョキ' and cpu_choice == 'パー') or \
         (user_choice == 'パー' and cpu_choice == 'グー'):
        result = 'あなたの勝ち！'
        win_count += 1
    else:
        result = 'あなたの負け！'
        lose_count += 1

        total_games += 1
    # 勝率を計算
    win_rate = (win_count / total_games) * 100

    return jsonify({
        'user_choice': user_choice,
        'cpu_choice': cpu_choice,
        'result': result,
        'win_rate': round(win_rate, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)