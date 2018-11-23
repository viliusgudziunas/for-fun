puts "Please enter an integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter another integer:"
print ">"
int2 = gets.chomp.to_i

if int1 == 11 || int2 == 11 || int1 + int2 == 11 || (int1-int2).abs == 11
  puts 11
else
  puts "These numbers ain't compatible"
end