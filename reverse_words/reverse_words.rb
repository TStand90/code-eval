def reverse_words(words)
  words = words.split(' ')
  words = words.reverse
  words.join(" ")
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    puts(reverse_words(line))
  end
end
