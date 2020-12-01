from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags) 

@tags_blueprint.route("/tags/<id>")    
def show(id):
    tag = tag_repository.select(id)
    tag_merchants = tag_repository.merchants(tag)
    return render_template("tags/show.html", tag=tag, tag_merchants=tag_merchants)


@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)


@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tags(id):
    category = request.form["category"]
    tag = Tag(category, id)
    tag_repository.update(tag)
    return redirect("/tags")