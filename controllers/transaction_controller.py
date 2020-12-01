from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", transactions=transactions, tags=tags)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    amount = request.form['amount']
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, tag, amount)
    transaction_repository.save(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_task(id):
    transaction_repository.delete(id)
    return redirect('/transactions')