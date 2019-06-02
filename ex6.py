x = "There are %d types of people." % 10
binary = "bianry"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I alse said: '%s'." % y

hilarious = False
joker_evaluation = "Isn't that joke so funny?! %r"

print joker_evaluation % hilarious

w = "This is the left of..."
e = "a string with a right side."

print w + e

# 用%r显示的是变量“原始”的数据值，%r在打印的时候能够重现它代表的对象，但其他的符号用来给用户显示变量值。
text = "I am %d years old." % 22
print "I said: %s." % text
print "I said: %r" % text