puts "Please enter a number:"
print ">"
n = gets.chomp.to_f

if n > 33
  puts 2 * (n - 33).abs
else
  puts (n - 33).abs
end