puts "Please enter a big integer:"
print ">"
num = gets.chomp
array = num.split("").map(&:to_i)

count = 0
array.each{|num| count += 1 unless num !=5}

puts count