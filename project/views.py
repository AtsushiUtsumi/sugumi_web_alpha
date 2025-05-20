from apps.app import db
from apps.project.forms import UserForm
from apps.project.models import User
from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

# Blueprintでprojectアプリを生成する
project = Blueprint(
    "project",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# indexエンドポイントを作成しindex.htmlを返す
@project.route("/")
@login_required
def index():
    return render_template("project/index.html")


@project.route("/sql")
@login_required
def sql():
    db.session.query(User).all()
    return "コンソールログを確認してください"


@project.route("/users/new", methods=["GET", "POST"])
@login_required
def create_user():
    # UserFormをインスタンス化する
    form = UserForm()

    # フォームの値をバリデートする
    if form.validate_on_submit():
        # ユーザーを作成する
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # ユーザーを追加してコミットする
        db.session.add(user)
        db.session.commit()

        # ユーザーの一覧画面へリダイレクトする
        return redirect(url_for("project.users"))
    return render_template("project/create.html", form=form)


@project.route("/users")
@login_required
def users():
    """ユーザーの一覧を取得する"""
    users = User.query.all()
    return render_template("project/index.html", users=users)


# methodsにGETとPOSTを指定する
@project.route("/users/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()

    # Userモデルを利用してユーザーを取得する
    user = User.query.filter_by(id=user_id).first()

    # formからサブミットされた場合はユーザーを更新しユーザーの一覧画面へリダイレクトする
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("project.users"))

    # GETの場合はHTMLを返す
    return render_template("project/edit.html", user=user, form=form)


@project.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("project.users"))
