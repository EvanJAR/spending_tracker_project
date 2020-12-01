from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag


#CREATE - new merchant
def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

#READ - select one by id
def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant 

#READ - select all merchants
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

#UPDATE 
#DELETE - all
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

#DELETE - one
def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def tags(merchant):
    tags = []
    sql = """SELECT tags.* FROM tags
                INNER JOIN transactions ON tags.id = transactions.tag_id
                INNER JOIN merchants ON merchants.id = transactions.merchants_id
                WHERE merchants.id = %s"""
    values = [merchant.id]
    sql_results = run_sql(sql, values)
    for row in sql_results:
        tag = Tag(row['category'], row['id'])
        tags.append(tag)
    return tags