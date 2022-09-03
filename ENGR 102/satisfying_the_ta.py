def closeCorrectst(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


l1 = [5,6,7]
    
closeCorrect = [4.794520547945206,11.917808219178081,7.698630136986301,7.904109589041096,-0.5479452054794507]

for i in range(len(l1)):
    if abs(closeCorrectst(closeCorrect, l1[i]) - l1[i]) < .000001:
        l1[i] = closeCorrectst(closeCorrect, l1[i])
 