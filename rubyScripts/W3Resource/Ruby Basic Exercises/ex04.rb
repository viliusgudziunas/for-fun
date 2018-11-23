puts "Please enter the radius of a circle:"
print ">"
r = gets.chomp.to_f

pi = Math::PI

puts "The perimeter is: #{'%.2f' % (2*pi*r)}"
puts "The area of a circle is: #{'%.2f' % (pi*(r**2))}"