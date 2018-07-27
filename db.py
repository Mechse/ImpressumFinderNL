import MySQLdb

db = MySQLdb.connect()                             # name of the data base


def GetDomains(sql):
    domains = list()

    cur = db.cursor()

    cur.execute(sql)

    for row in cur.fetchall():
        domains.append(row[1])

    return domains
