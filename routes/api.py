from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Regist, User, Subject
from peewee import *

# Blueprintの作成
api_bp = Blueprint('api', __name__, url_prefix='/api')

# 返す型はjson
# 教科ごとの履修登録者を返す
# key=教科名, value=履修者の数
# @api_bp.route('/register_summary_bar', methods=['GET', 'POST'])
# def register_summary_bar():
#     '''
#     query = (
#         Regist.select(
#             Subject.name #科目名
#         )
#         .join(Subject, on=(Subject.name == Regist.subject))  # 明示的にProductとの結合条件を指定
#         .group_by(Subject.name)  # 履修登録した生徒ごとにグループ化
#         .order_by(fn.COUNT(Regist.user))  # 履修登録した生徒数
#     )
#     '''
#     print('pass')
#     query = (
#         Regist.select(Subject.name)  # 科目名を選択
#         .join(Subject, on=(Subject.name == Regist.subject))  # 結合条件を指定
#         .group_by(Subject.name)  # 科目名でグループ化
#     )
    
#     grouped_count = len(list(query))

#     print(query)
#     # ここに書く

# # 返す型はjson
# # 教科ごとの履修登録者を返す
# # key=教科名, value=その科目の履修者の数 但し、TOP5のみ返す
# @api_bp.route('/register_summary_ranking', methods=['GET', 'POST'])
# def register_summary_ranking():
#     # ここに書く
#     pass

# 返す型はjson
# 生徒ごとに履修合計単位数を返す
# key=生徒名, value=その生徒の合計単位数
@api_bp.route('/credit_summary_bar', methods=['GET', 'POST'])
def credit_summary_bar():
    query = (
        Regist.select(
            User.name, 
            fn.SUM(Subject.price).alias('total_credits')
        )
        .join(User, on=(Regist.user == User.id))
        .join(Subject, on=(Regist.subject == Subject.id))
        .group_by(Regist.user)
        .order_by(fn.SUM(Subject.price).desc())  # 合計単位数が多い順にソート
    )
    
    students_data = {result.user.name: result.total_credits for result in query}
    
    result = {
        'labels': list(students_data.keys()),
        'data': list(students_data.values())
    }
    
    return jsonify(result)
    
# 返す型はjson
# 生徒ごとに履修合計単位数を返す
# key=生徒名, value=その生徒の合計単位数 但し、TOP5のみ返す
# @api_bp.route('/credit_summary_ranking', methods=['GET', 'POST'])
# def credit_summary_ranking():
#     query = (
#         User.select(
#             User.name, fn.SUM(Subject.price).alias('student_data')
#         )
#         .join(Regist, on=(User.name == Regist.user))
#         .join(Subject, on=(Regist.subject == Subject.name))
#         .group_by(User.name)
#         .order_by(fn.SUM(Subject.price).desc())
#     )

#     # 上位5名の結果を表示
#     students_data = {user.name: user.total_credits for user in  enumerate(query.limit(5), start=1)}
    
#     result = {
#         'labels': list(students_data.keys()),
#         'data': list(students_data.values())
#     }
#     return jsonify(result)
