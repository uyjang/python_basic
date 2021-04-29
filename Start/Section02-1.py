# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Sepatator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome to', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 옵션 사용 []대괄호, {}중괄호, ()소괄호
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('Jang', 7)) # %s : 문자 , %d : 정수 , %f : 실수

print("Test1: %5d, price: %4.2f" % (776,6534.123))
print("Test1: {0:5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

# escape 사용

print("'You'")
print('\'You\'')
print('"You"')
print("""'You'""")
print('\\You\\\n')
print('\t\t\ttest')