puts "Please enter numbers for the following:"

print "> x = "
x = gets.chomp.to_i
print "> y = "
y = gets.chomp.to_i
print "> z = "
z = gets.chomp.to_i

puts "Max: #{[x, y, z].max}"