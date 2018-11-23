puts "Please enter an integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter another integer:"
print ">"
int2 = gets.chomp.to_i

if (10 - int1).abs == (10 - int2).abs
  puts 0
elsif (10 - int1).abs < (10 - int2).abs
  puts int1
else
  puts int2
end