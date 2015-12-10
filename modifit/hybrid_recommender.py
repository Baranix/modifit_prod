import db_connector
import numpy as np
from math import sqrt


# cosine similarity of 2 users based on their set of items
def getCosineSimilarity( user1, user2 ):
    dot = np.dot(user1, user2)
    vectors = sqrt( np.sum( user1**2 ) ) * sqrt( np.sum( user2**2 ) )
    result = dot / vectors

    return result


# converts a set of items into a vector
def getOrderedValues( user1, user2 ):
    # union of 2 sets of items
    union = sorted(list(set(user1) | set(user2)))

    orderedValues = []
    for k in union:
        if k in user1.keys():
            orderedValues.append(user1[k])
        else:
            orderedValues.append(0)

    return orderedValues


# gets the k nearest neighbors based on their similarity scores
def kNN( similarities, k ):
    top = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:k]

    NN = []
    for n in top:
        NN.append(n[0])

    return NN


# generate the corresponding weight of each nearest neighbor
def assignWeights( NN, similarities ):
    totalWeight = 0

    for n in NN:
        totalWeight = totalWeight + similarities[n]

    weights = {}
    for n in NN:
        weights[n] = (similarities[n] / totalWeight)

    return weights


# compute the weighted ratings of the items owned by the nearest neighbors
def getWeightedRatings( currentUser, category, similarities, wardrobes ):
    k = 5

    weightedRatings = {}

    NN = kNN( similarities, k )
    weights = assignWeights( NN, similarities )

    for k in weights.keys():
        wardrobe = wardrobes[k][category]
        for item in wardrobe:
            if item not in wardrobes[currentUser][category]:
                if item not in weightedRatings:
                    weightedRatings[item] = (wardrobe[item] * weights[k])
                else:
                    weightedRatings[item] += (wardrobe[item] * weights[k])

    return weightedRatings


# jaccard index of 2 items based on their set of attributes
def getJaccardIndex(item1, item2):
    intersect = len(set(item1) & set(item2))
    union = len(set(item1) | set(item2))
    jaccard = intersect / float(union)
    return jaccard


def main():
    conn = db_connector.getDBConnection()
    cur = conn.cursor()

    wardrobes = db_connector.getAllWardrobeData()
    catalogue = db_connector.getCatalogueData()

    users = sorted(wardrobes.keys())
    for user in users:
        # comment when not updating db
        #query = "DELETE FROM modifit_user_recommendations WHERE user_id = {0}"
        #cur.execute(query.format(user))

        print "user: " + str(user)

        for category in range(1, 15):
            if category in wardrobes[user]:
                print "category: " + str(category)

                # compute cosine similarities under the current category
                cosineSimilarities = {}
                for user2 in users:
                    if user2 != user and category in wardrobes[user2]:
                        a = getOrderedValues( wardrobes[user][category], wardrobes[user2][category] )
                        b = getOrderedValues( wardrobes[user2][category], wardrobes[user][category] )
                        cosineSimilarities[user2] = getCosineSimilarity( np.array( a ), np.array( b ) )
                        #print str(user2) + ": " +  str(cosineSimilarities[user2])
                #print kNN( cosineSimilarities, 5 )

                # compute weighted ratings of items from nearest neighbors
                weightedRatings = getWeightedRatings( user, category, cosineSimilarities, wardrobes )
                #print weightedRatings

                # pick the top 3 weighted ratings
                sortedRatings = sorted(weightedRatings.items(), key=lambda x: x[1], reverse=True)
                if len(sortedRatings) > 3:
                    sortedRatings = sortedRatings[:3]

                # assign the top 3 as candidate items
                candidateItems = {}
                for rating in sortedRatings:
                    candidateItems[rating[0]] = rating[1]
                #print candidateItems

                # compute projected ratings of candidate items using jaccard index
                # if projected rating >= 3, then item will be recommended to user
                projectedRatings = {}
                for item1 in candidateItems:
                    for item2 in wardrobes[user][category]:
                        score = getJaccardIndex(catalogue[category - 1][item1], catalogue[category - 1][item2])
                        rating = score * wardrobes[user][category][item2]
                        if (item1 not in projectedRatings or score > projectedRatings[item1]) and rating >= 3:
                            projectedRatings[item1] = rating
                #print projectedRatings

                # print recommendations and projected ratings
                for item in sorted(projectedRatings.keys()):
                   print str(item) + ": " + str(projectedRatings[item])

                # comment when not updating db
                """for item in catalogue[category - 1]:
                    if item in projectedRatings:
                        query = "INSERT INTO modifit_user_recommendations " \
                              + "(user_id, item_id, projected_rating, user_rating) " \
                              + "VALUES ({0}, {1}, {2}, 0);"
                        try:
                            cur.execute(query.format(user, item, projectedRatings[item]))
                        except:
                            print "Can't execute query"""
            print

    # comment when not updating db
    #conn.commit()
    #conn.close()

main()