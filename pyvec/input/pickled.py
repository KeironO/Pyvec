import cPickle as pickle

def pickle_in(directory):
    test_data = None
    test_labels = None
    train_data, train_labels, val_data, val_labels, test_data, test_labels = pickle.load(open(directory+"/pdata.p", 'rb'))
    return train_data, train_labels, val_data, val_labels, test_data, test_labels
   
  