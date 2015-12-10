import psycopg2


def getDBConnection():
    try:
        conn = psycopg2.connect(
            database='d5914cigeuchlr',
            user='rvcgzocqxdmppm',
            password='b-wim0PggajRFhcwO_NiEnjvtW',
            host='ec2-54-204-7-145.compute-1.amazonaws.com',
            port='5432'
        )
    except:
        print "Can't connect to the database"
    return conn


# retrieves all wardrobe data, stored as a dictionary
# format: wardrobes[user_id][category_id][item_id] = item rating
def getAllWardrobeData():
    conn = getDBConnection()

    cur = conn.cursor()
    try:
        query = "SELECT user_id, category_id, ARRAY_AGG(modifit_wardrobe.item_id), ARRAY_AGG(rating) " \
            + "FROM modifit_wardrobe, modifit_hascategory, auth_user  " \
            + "WHERE modifit_wardrobe.user_id = auth_user.id  " \
            + "AND modifit_hascategory.item_id = modifit_wardrobe.item_id " \
            + "AND auth_user.is_active != 'f'  " \
            + "GROUP BY user_id, category_id  " \
            + "HAVING sum(rating) != 0 "\
            + "ORDER BY user_id, category_id "
        cur.execute(query)
    except:
        print "Can't execute query"

    wardrobes = {}
    rows = cur.fetchall()
    for row in rows:
        ratings = {}
        if row[0] not in wardrobes:
            wardrobes[row[0]] = {}
        for i in range(len(row[2])):
            ratings[row[2][i]] = row[3][i]
        wardrobes[row[0]][row[1]] = ratings
    return wardrobes


# retrieves all item data, stored as a list of categories
# format: catalogue[category_id - 1][item_id] = dictionary of item attributes
def getCatalogueData():
    conn = getDBConnection()

    cur = conn.cursor()

    query = "SELECT modifit_item.id, " \
          + "       ARRAY_AGG(modifit_hasattribute.attribute_type), " \
          + "       ARRAY_AGG(modifit_hasattribute.attribute_id) " \
          + "FROM modifit_item, " \
          + "     modifit_hascategory, " \
          + "     modifit_hasattribute " \
          + "WHERE modifit_item.id = modifit_hasattribute.item_id " \
          + "  AND modifit_item.id = modifit_hascategory.item_id " \
          + "  AND modifit_hascategory.category_id = {0} " \
          + "GROUP BY modifit_item.id " \
          + "ORDER BY modifit_item.id;"

    catalogue = []
    for cat_id in range(1, 15):
        try:
            cur.execute(query.format(cat_id))
        except:
            print "Can't execute query"

        items = {}
        rows = cur.fetchall()
        for row in rows:
            attributes = []
            for i in range(len(row[1])):
                attributes.append((row[1][i], row[2][i]))
            items[row[0]] = attributes
        catalogue.append(items)
    return catalogue
