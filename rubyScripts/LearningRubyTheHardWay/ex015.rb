# takes the user input from the call
filename = ARGV.first

# opens the file
txt = open(filename)

# prints the name of the file
puts "Here's your file #{filename}:"
# prints the contents of a file
puts txt.read

# prints a line to ask for more user input
print "Type the filename again: "
# gets the name of another file
file_again = $stdin.gets.chomp

# opens the new file
txt_again = open(file_again)

# prints the contents of the new file
puts txt_again.read