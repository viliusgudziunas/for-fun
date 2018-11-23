# Animal is-a object look at the extra credit
class Animal
end

# Dog is-a Animal object
class Dog < Animal

  def initialize(name)
    # Dog has-a name attribute
    @name = name
  end

end

# Cat is-a Animal object
class Car < Animal

  def initialize(name)
    # Cat has-a name attribute
    @name = name
  end

end

# Person is-a object
class Person

  def initialize(name)
    # Person has-a name attribute
    @name = name

    # Person has-a pet of some kind
    @pet = nil
  end

  attr_accessor :pet

end

# Employee is-a Person object
class Employee < Person

  def initialize(name, salary)
    # Employee has-a name attribute that is defined in parent class
    super(name)
    # Employee has-a salary attribute
    @salary = salary
  end

end

# Fish is-a object
class Fish
end

# Salmon is-a Fish object
class Salmon < Fish
end

# Halibut is-a Fish object
class Halibut < Fish
end

# Rover is-a Dog object and thus an Animal object
rover = Dog.new("Rover")

# Satan is-a Cat object and thus an Animal object
satan = Cat.new("Satan")

# Mary is-a Person object
mary = Person.new("Mary")

# Mary has-a Pet attribute of satan
mary.pet = satan

# Frank is-a Employee object and thus a Person object
frank = Employee.new("Frank", 120000)

# Frank has-a Pet attribute of rover
frank.pet = rover

# Flipper is-a Fish object
flipper = Fish.new

# Crouse is-a Salmon object and thus a Fish object
crouse = Salmon.new

# Harry is-a Halibut object and thus a Fish object
harry = Halibut.new