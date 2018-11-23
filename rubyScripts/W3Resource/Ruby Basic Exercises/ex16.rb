puts "Please enter your age:"
print ">"
age = gets.chomp.to_i

if age <= 18
  puts "You are a minor, get away from me!"
else
  puts "You are an adult, how's it going?"
end