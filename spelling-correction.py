import editdistance
import  ngram
import  soundex

#read the dictionary
def getDictionary():
    dict_list = []
    f = open("dict.txt",'r')
    for line in f:
        dict_list.append(line.strip())
    return dict_list

#read the token
def getTweetsToken():
    token_list = []
    tag_list = []
    correction_list = []
    f = open("labelled-tokens.txt",'r')
    for line in f:
        l = line.split()
        token_list.append(l[0].strip())
        tag_list.append(l[1].strip())
        correction_list.append(l[2].strip())
    result_list = [token_list,tag_list,correction_list]
    return result_list

#process by editdistance
def globalEditDistance(string,dict_list):
    best_val = 9999999999999
    best_str = ""
    for line in dict_list:
        val = editdistance.eval(string,line)
        if val < best_val:
            best_val = val
            best_str = line
    return best_str

#process by ngram
def ngramDistance(string,dict_list):
    G = ngram.NGram(dict_list)
    return G.find(string)

#process by soundex
def soundexTest(string,dict_list):
    instance = soundex.getInstance()
    for line in dict_list:
        val = instance.compare(string,line)
        if val == 1:
            return val

#main function
if __name__ == '__main__':
    #initial process
    dict_list = getDictionary()
    result_list = getTweetsToken()
    token_list = result_list[0]
    tag_list = result_list[1]
    correction_list = result_list[2]

    #editdistance process
    # editdistance_result = []
    # for index in range(len(token_list)):
    #     if tag_list[index] == "OOV" or tag_list[index] == "NO":
    #         editdistance_result.append(token_list[index])
    #         print token_list[index]
    #     else:
    #         editdistance_result.append(globalEditDistance(token_list[index],dict_list))
    #         print "sunshibo"
    # f = file("editdistance.txt","w")
    # for i in range(len(editdistance_result)):
    #     editdistance_result[i] = editdistance_result[i]+"\n"
    # f.writelines(editdistance_result)

    #ngram process
    ngram_result = []
    for index in range(len(token_list)):
        if tag_list[index] == "OOV" or tag_list[index] == "NO":
            ngram_result.append(token_list[index])
            print token_list[index]
        else:
            ngram_result.append(ngramDistance(token_list[index],dict_list))
            print "sunshibo"
    f = file("ngramresult.txt","w")
    for i in range(len(ngram_result)):
        ngram_result[i] = ngram_result[i]+"\n"
    f.writelines(ngram_result)
