def lowest_unique_number(line)
  numbers = line.split(' ')
  number_counts = Hash.new(0)

  numbers.each do |number|
    number_counts[number.to_i] += 1
  end

  winning_number = 10

  number_counts.each do |key, value|
    if key < winning_number and value == 1
      winning_number = key
    end
  end

  if winning_number == 10
    return 0
  else
    numbers.each_with_index do |number, index|
      if number.to_i == winning_number
        return index + 1
      end
    end
  end
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    puts lowest_unique_number(line.chomp)
  end
end
