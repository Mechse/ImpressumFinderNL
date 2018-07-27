import MySQLdb

db = MySQLdb.connect(host="stat.byte.at",                   # your host, usually localhost
                     user="root",                           # your username
                     passwd="jDLj83LID#23khj823",           # your password
                     db="stat")                             # name of the data base


def GetDomains(sql):
    domains = list()

    cur = db.cursor()

    cur.execute(sql)

    for row in cur.fetchall():
        domains.append(row[1])

    return domains
