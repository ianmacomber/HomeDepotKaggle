import numpy as np
import pandas as pd

df_train = pd.read_csv('/Users/ianmacomber/HomeDepotKaggle/Data/train.csv', encoding="ISO-8859-1")
df_test = pd.read_csv('/Users/ianmacomber/HomeDepotKaggle/Data/test.csv', encoding="ISO-8859-1")
df_product_descriptions = pd.read_csv('/Users/ianmacomber/HomeDepotKaggle/Data/product_descriptions.csv', encoding="ISO-8859-1")
df_attributes = pd.read_csv('/Users/ianmacomber/HomeDepotKaggle/Data/attributes.csv', encoding="ISO-8859-1")

print(df_train.shape)                 # (74067, 5)
print(df_test.shape)                  # (166693, 4)
print(df_product_descriptions.shape)  # (124428, 2)
print(df_attributes.shape)            # (2044803, 3)

'''
df_train.dtypes

id                 int64
product_uid        int64
product_title     object
search_term       object
relevance        float64

    id  product_uid product_title                                         search_term         relevance
0   2       100001  Simpson Strong-Tie 12-Gauge Angle                     angle bracket       3.00
1   3       100001  Simpson Strong-Tie 12-Gauge Angle                     bracket             2.50
2   9       100002  BEHR Premium Textured DeckOver 1-gal. #SC-141 ...     deck over           3.00
3  16       100005  Delta Vero 1-Handle Shower Only Faucet Trim Ki...     rain shower head    2.33
4  17       100005  Delta Vero 1-Handle Shower Only Faucet Trim Ki...     shower only faucet  2.67

df_product_descriptions.dtypes

product_uid             int64
product_description    object
dtype: object

        product_uid                                product_description
0       100001  Not only do angles make joints stronger, they ...
1       100002  BEHR Premium Textured DECKOVER is an innovativ...
2       100003  Classic architecture meets contemporary design...
3       100004  The Grape Solar 265-Watt Polycrystalline PV So...
4       100005  Update your bathroom with the Delta Vero Singl...

df_attributes.dtypes

product_uid    float64
name            object
value           object

  product_uid      name                                              value
0       100001  Bullet01  Versatile connector for various 90Â° connectio...
1       100001  Bullet02  Stronger than angled nailing or screw fastenin...
2       100001  Bullet03  Help ensure joints are consistently straight a...
3       100001  Bullet04              Dimensions: 3 in. x 3 in. x 1-1/2 in.
4       100001  Bullet05                           Made from 12-Gauge steel
'''
