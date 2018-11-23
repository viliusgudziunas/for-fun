puts "Please enter a number:"
print ">"
num = gets.chomp.to_i

if 100 - num.abs <= 10
  puts "The number is withing 10 of 100"
elsif 200 - num.abs <= 10
  puts "The number is within 10 of 200"
else
  puts "The number is meh"
end