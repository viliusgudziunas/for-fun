puts "Please enter full path to a ruby file:"
print ">"
file = gets.chomp

file_name = File.basename file
puts "File name: #{file_name}"

base_name = File.basename file, ".rb"
puts "Base name: #{base_name}"

file_extension = File.extname file
puts "File extension: #{file_extension}"

path_name = File.dirname file
puts "Path name: #{path_name}"