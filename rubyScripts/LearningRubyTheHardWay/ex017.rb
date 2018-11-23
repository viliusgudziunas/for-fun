from_file, to_file = ARGV

puts "Copying from #{from_file} to #{to_file}"

# we could do these two on one line, how?
in_data = open(from_file).read

puts "The input file is #{in_data.length} bytes long"

puts "Does the output file exist? #{File.exist?(to_file)}"

open(to_file, "w").write(in_data)

puts "Alright, all done."