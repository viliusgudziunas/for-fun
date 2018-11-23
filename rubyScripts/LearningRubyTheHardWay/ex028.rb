print "1. "
puts true && true

print "2. "
puts false && true

print "3. "
puts 1 == 1 && 2 == 1

print "4. "
puts "test" == "test"

print "5. "
puts 1 == 1 || 2 != 1

print "6. "
puts true && 1 == 1

print "7. "
puts false && 0 != 0

print "8. "
puts true || 1 == 1

print "9. "
puts "test" == "testing"

print "10. "
puts 1 != 0 && 2 == 1

print "11. "
puts "test" != "testing"

print "12. "
puts "test" == 1

print "13. "
puts !(true && false)

print "14. "
puts !(1 == 1 && 0 != 1)

print "15. "
puts !(10 == 1 || 1000 == 1000)

print "16. "
puts !(1 != 10 || 3 == 4)

print "17. "
puts !("testing" == "testing" && "Zed" == "Cool Guy")

print "18. "
puts 1 == 1 && (!("testing" == 1 || 1 == 0))

print "19. "
puts "chunky" == "bacon" && (!(3 == 4 || 3 == 3))

print "20. "
puts 3 == 3 && (!("testing" == "testing" || "Ruby" == "Fun"))
