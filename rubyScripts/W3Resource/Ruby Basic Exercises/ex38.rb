puts "Please enter an integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter another integer:"
print ">"
int2 = gets.chomp.to_i

first = int1 >= 20 && int1 <= 30
second = int2 >= 20 && int2 <= 30

if first && second
  if int1 > int2
    puts int1
  elsif int2 > int1
    puts int2
  else
    puts "Both numbers are in range and equal"
  end
elsif first
  puts int1
elsif second
  puts int2
else
  puts 0
end