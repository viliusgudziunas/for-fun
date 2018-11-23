puts "Please enter an integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter another integer:"
print ">"
int2 = gets.chomp.to_i

if int1 + int2 >= 20 && int1 + int2 <=30
  puts 30
else
  puts int1 + int2
end