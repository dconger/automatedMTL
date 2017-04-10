import cPickle as pickle
import os
from os.path import expanduser
from os.path import basename

def class_look_up(data_path):
    out_train = open(expanduser(data_path+"/train_classes.txt"), "w")
    out_test = open(expanduser(data_path+"/test_classes.txt"), "w")
    train_folders = os.listdir(expanduser(data_path+"/Train/"))
    test_folders = os.listdir(expanduser(data_path+"/Test/"))
    if "rotten_tomato" not in data_path:
        validation_folders = os.listdir(expanduser(data_path+"/Validation/"))
        out_val = open(expanduser(data_path+"/validation_classes.txt"), "w")
 
    dict = {"World": 0, "Sports": 1, "Business":2, "Sci_Tech":3}
    cnt = 0
    file2class_dict = {}

    for i in train_folders:
        if i[0] != '.':
            #if dict.get(i) == None:
	    #    dict[i] = cnt
            #    cnt += 1
            files = os.listdir(expanduser(data_path+"/Train/"+i))
	    for f in files:
                if f[0] == ".": continue
	        out_train.write(f[0:len(f) - 4] + "   " + i + "   " + str(dict[i]))
                out_train.write("\n") 
                file2class_dict[int(f[0:len(f) - 4])] = (i, dict[i])

    for i in test_folders:
        if i[0] != '.':
            files = os.listdir(expanduser(data_path+"/Test/"+i))
	    for f in files:
                if f[0] == ".": continue
	        out_test.write(f[0:len(f) - 4] + "   " + i + "   " + str(dict[i]))
		out_test.write("\n")
                file2class_dict[int(f[0:len(f) - 4])] = (i, dict[i])
    

    if "rotten_tomato" not in data_path:
        for i in validation_folders:
            if i[0] != '.':
                files = os.listdir(expanduser(data_path+"/Validation/"+i))
	        for f in files:
                    if f[0] == ".": continue
	            out_val.write(f[0:len(f) - 4] + "   " + i + "   " + str(dict[i]))
		    out_val.write("\n")
                    file2class_dict[int(f[0:len(f) - 4])] = (i, dict[i])
	out_val.close()
    out_train.close()
    out_test.close()
    pickle.dump(file2class_dict, open(expanduser(data_path+"/classes.pkl"), "w"))
    #print file2class_dict
    #print len(file2class_dict)

if __name__ == "__main__":
    #class_look_up("~/automatedMTL/data/rotten_tomato")
    class_look_up("~/tweetnet/automatedMTL/data/ag_news_csv")
