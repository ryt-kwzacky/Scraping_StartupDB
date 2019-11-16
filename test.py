import pandas as pd

# run this process at first
# comment out this after second process
df = pd.DataFrame([], columns=['name', 'address', 'URL', 'employee', 'foundation', 'Total Fundraising'])
df.to_csv("test.csv", encoding='utf_8_sig')

testArray1 = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6']
s = pd.DataFrame(testArray1, index=['name', 'address', 'URL', 'employee', 'foundation', 'Total Fundraising'])
s.T.to_csv('test.csv', encoding='utf_8_sig', mode='a', header=False)

testArray2 = ['test7', 'test8', 'test9', 'test10', 'test11', 'test12']
s = pd.DataFrame(testArray2, index=['name', 'address', 'URL', 'employee', 'foundation', 'Total Fundraising'])
s.T.to_csv('test.csv', encoding='utf_8_sig', mode='a', header=False)
