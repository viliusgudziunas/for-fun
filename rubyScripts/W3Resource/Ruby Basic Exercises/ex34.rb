puts "Please enter a string:"
print ">"
string = gets.chomp

string1 = string.downcase
first_char = string[0]

if string1[1..4] == "java"
  puts first_char + string[5, string.length]
else
  puts string
end