def remove_characters(sentence, chars)
  sentence.delete(chars)
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    sentence, chars = line.split(", ")
	puts(remove_characters(sentence, chars))
  end
end
