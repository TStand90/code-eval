def penultimate_word(words)
  words.split(" ")[-2]
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    puts penultimate_word(line)
  end
end
