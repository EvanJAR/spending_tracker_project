from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag


#CREATE - new tag
def save(tag):
    sql = "INSERT INTO tags (category) VALUES (%s) RETURNING id"
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

#READ - select one by id
def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['category'], result['id'])
    return tag 

#READ - select all merchants
def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['category'], row['id'])
        tag.append(tag)
    return tags

#UPDATE 
#DELETE - all
def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

#DELETE - one
def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def merchants(tag):
    results = []
    sql = """SELECT merchants.*
                FROM merchants
                INNER JOIN transactions ON merchants.id = transactions.merchant_id
                INNER JOIN tags ON tags.id = transactions.tag_id
                WHERE tags.id = %s"""
    values = [tag.id]
    sql_results = run_sql(sql, values)
    for row in sql_results:
        merchant = Merchant(row['name'], row['id'])
        results.append(merchant)
    return results