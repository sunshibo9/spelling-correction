# spelling-correction
Lexical Normalisation of Twitter Data

This code include three pachage which are editdistance, ngram and soundex respectively.
editdistance is from https://www.github.com/aflc/editdistance
ngram is from http://github.com/gpoulter/python-ngram
soundex is from https://github.com/Project-SILPA/soundex

There are totally six funcation and a main function in the programme.
getDictionary() is to save the data from "dict.txt" to list.
getTweetsToken() is to save the token from "labelled-token.txt" to list
globalEditDistance() is using the editdistance package to get a list of the best match of the token.
ngramDistance is using ngram package to get the matching words from dictionary.
soundexTest() is using soundex to get the best match.
calculationAccuracy() is to calculate the accuracy of the result. 
