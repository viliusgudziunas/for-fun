print "Give me a some money: "
money = gets.chomp.to_f

puts "Here is a 10% - #{'%.2f' % (money * 0.1)}."