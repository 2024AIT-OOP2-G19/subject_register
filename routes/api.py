from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Regist, User, Subject
from peewee import *

# Blueprintの作成
api_bp = Blueprint('api', __name__, url_prefix='/api')

# 返す型はjson
# 教科ごとの履修登録者を返す
# key=教科名, value=履修者の数
@api_bp.route('/register_summary_bar', methods=['GET', 'POST'])
def register_summary_bar():
    query = (
        Regist.select(
            Subject.name, 
            fn.COUNT(Regist.user).alias('user_count')
        )
        .join(Subject, on=(Subject.id == Regist.subject))
        .group_by(Subject.name)
        .order_by(fn.COUNT(Regist.user).desc())
    )

    regist_data = {result.subject.name: result.user_count for result in query}

    # JSON形式で返す
    result = {
        'labels': list(regist_data.keys()),
        'data': list(regist_data.values())
    }

    return jsonify(result)

# 返す型はjson
# 教科ごとの履修登録者を返す
# key=教科名, value=その科目の履修者の数 但し、TOP5のみ返す
@api_bp.route('/register_summary_ranking', methods=['GET', 'POST'])
def register_summary_ranking():
    query = (
        Regist.select(
            Subject.name, 
            fn.COUNT(Regist.user).alias('user_count')
        )
        .join(Subject, on=(Subject.id == Regist.subject))
        .group_by(Subject.name)
        .order_by(fn.COUNT(Regist.user).desc())
        .limit(5)
    )

    regist_data = {result.subject.name: result.user_count for result in query}

    # JSON形式で返す
    result = {
        'labels': list(regist_data.keys()),
        'data': list(regist_data.values())
    }

    return jsonify(result)


# 返す型はjson
# 生徒ごとに履修合計単位数を返す
# key=生徒名, value=その生徒の合計単位数
@api_bp.route('/credit_summary_bar', methods=['GET', 'POST'])
def credit_summary_bar():
    query = (
        Regist.select(
            User.name, #生徒名
            fn.SUM(Subject.price).alias('total_credits') # 生徒ごとに合計単位数
        )
        .join(User, on=(Regist.user == User.id))  # 明示的にUserとの結合条件を指定
        .join(Subject, on=(Regist.subject == Subject.id))  # 明示的にSubjectとの結合条件を指定
        .group_by(Regist.user) # 生徒ごとにグループ化
        .order_by(fn.SUM(Subject.price).desc())  # 合計単位数が多い順にソート
    )
    
    students_data = {result.user.name: result.total_credits for result in query}
    
    result = {
        'labels': list(students_data.keys()),
        'data': list(students_data.values())
    }
    print(result)
    
    return jsonify(result)
    
# 返す型はjson
# 生徒ごとに履修合計単位数を返す
# key=生徒名, value=その生徒の合計単位数 但し、TOP5のみ返す
@api_bp.route('/credit_summary_ranking', methods=['GET', 'POST'])
def credit_summary_ranking():
    # queryは上のcredit_summary_barと同じ
    query = (
        Regist.select(
            User.name, 
            fn.SUM(Subject.price).alias('total_credits')
        )
        .join(User, on=(Regist.user == User.id))
        .join(Subject, on=(Regist.subject == Subject.id))
        .group_by(Regist.user)
        .order_by(fn.SUM(Subject.price).desc())
    )

    # 上位5名の結果を表示
    students_data = { f'rank {rank}:{result.user.name}' : result.total_credits for rank, result in enumerate(query.limit(5), start=1)}
    
    result = {
        'labels': list(students_data.keys()),
        'data': list(students_data.values())
    }
    return jsonify(result)
