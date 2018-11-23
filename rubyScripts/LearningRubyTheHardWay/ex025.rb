module Ex025

  # This function will break up words for us.
  def Ex025.break_words(stuff)
    words = stuff.split(' ')
    return words
  end

  # Sorts the words.
  def Ex025.sort_words(words)
    return words.sort
  end

  # Prints the first word after shifting it off.
  def Ex025.print_first_word(words)
    word = words.shift
    puts word
  end

  # Prints the last word after popping it off.
  def Ex025.print_last_word(words)
    word = words.pop
    puts word
  end

  # Takes in a full sentence and returns the sorted words.
  def Ex025.sort_sentence(sentence)
    words = Ex025.break_words(sentence)
    return Ex025.sort_words(words)
  end

  # Prints the first and last words of the sentence.
  def Ex025.print_first_and_last(sentence)
    words = Ex025.break_words(sentence)
    Ex025.print_first_word(words)
    Ex025.print_last_word(words)
  end

  # Sorts the words then prints the first and last one.
  def Ex025.print_first_and_last_sorted(sentence)
    words = Ex025.sort_sentence(sentence)
    Ex025.print_first_word(words)
    Ex025.print_last_word(words)
  end

end