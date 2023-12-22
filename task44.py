# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Надо это сделать без get_dummieНs.

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()





import pandas as pd
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
one_hot_encoded = encoder.fit_transform(data[['whoAmI']].values.reshape(-1, 1)).toarray()
one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(['whoAmI']))