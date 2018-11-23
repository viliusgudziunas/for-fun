puts "Please enter a radius of the sphere:"
print ">"
r = gets.chomp.to_f

pi = Math::PI

puts "The volume of the sphere: #{'%.2f' % ((4.0 / 3.0) * pi * (r ** 3))}"