## TEXT SEARCH ENGINE

The main goal is to build a system trained on news dataset that should be able to find the closest paper title associated with the question/search word  and respond back with other required information as intended by the user.

## TFIDF Algorithm
1. Text cleaning and preprocessing dataset
2. Tokenize and create TF-IDF weight of whole dataset
3. Check against TF-IDF from trained dictionary
4. Calculate cosine similarity( between document and query)

## Backend
Flask was used to deploy this as a webservice where a title/subject is returned to a get API request.
