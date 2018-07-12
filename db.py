def getURLs(limit):
    import MySQLdb

    db = MySQLdb.Connection(host="stat.byte.at", user="root",
                            passwd="jDLj83LID#23khj823", db="stat")
    db.query("""SELECT name FROM host ORDER BY id LIMIT """ + str(limit))
    result = db.store_result()

    domains = []

    for i in range(result.num_rows()):
        domains.append(result.fetch_row()[0][0])

    return(domains)
