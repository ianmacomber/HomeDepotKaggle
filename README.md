## Home Depot Product Search Relevance

This is a code repo for the [Home Depo Kaggle Competition](https://www.kaggle.com/c/home-depot-product-search-relevance)

In this competition, Home Depot is asking Kagglers to help them improve their customers' shopping experience by developing a model that can accurately predict the relevance of search results.

## File Descriptions

These files can be found through the website and are stored in a `/Data` folder that is not committed to git.

* `train.csv` - the training set, contains products, searches, and relevance scores.
* `test.csv` - the test set, contains products and searches. You must predict the relevance for these pairs.
* `product_descriptions.csv` - contains a text description of each product. You may join this table to the training or test set via the product\_uid.
* `attributes.csv` - provides extended information about a subset of the products (typically representing detailed technical specifications). Not every product will have attributes.
* `sample_submission.csv` - a file showing the correct submission format.
* `relevance_instructions.docx` - the instructions provided to human rates.

## Data Fields

* `id` - a unique Id field which represents a (search\_term, product\_uid) pair
* `product_uid` -an id for the products
* `product_title` - the product title
* `product_description` - the text description of the product (may contain HTML content)
* `search_term` - the search query
* `relevance` - the average of the relevance ratings for a given id
* `name` - an attribute name
* `value` - the attribute's value

## Current State

No submissions

Current leaderboard score of 0.45886

## To-do

* Read up on ntlk for Python
* Top scripts on Kaggle use ntlk stems, tfid vectorizers
* Snowball stemmer and Porter Stemmer
