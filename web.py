# Blueprint をインポート
from flask import Blueprint, redirect, url_for

# Blueprint 名と関数名を同じにしてしまって落ちるのは初心者あるあるなのかもしれない
health_blueprint = Blueprint('health', __name__)

@health_blueprint.route("/health", methods=["GET"])
def health():
    return "HOGE"

