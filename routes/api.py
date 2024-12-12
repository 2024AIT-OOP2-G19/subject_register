from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Order, User, Product
from peewee import *

# Blueprintの作成
api_bp = Blueprint('api', __name__, url_prefix='/api')

# 返す型はjson
# 教科ごとの履修登録者を返す
# key=教科名, value=履修者の数
@api_bp.route('/register_summary_bar', methods=['GET', 'POST'])
def register_summary_bar():
    # ここに書く

# 返す型はjson
# 教科ごとの履修登録者を返す
# key=教科名, value=その科目の履修者の数 但し、TOP5のみ返す
@api_bp.route('/register_summary_ranking', methods=['GET', 'POST'])
def register_summary_ranking():
    # ここに書く
    
# 返す型はjson
# 生徒ごとに履修合計単位数を返す
# key=生徒名, value=その生徒の合計単位数
@api_bp.route('/credit_summary_bar', methods=['GET', 'POST'])
def credit_summary_bar():
    # ここに書く

# 返す型はjson
# 生徒ごとに履修合計単位数を返す
# key=生徒名, value=その生徒の合計単位数 但し、TOP5のみ返す
@api_bp.route('/credit_summary_ranking', methods=['GET', 'POST'])
def credit_summary_ranking():
    # ここに書く
