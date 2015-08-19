def check_digit(digit)
  double_of_digit = digit * 2
  if double_of_digit >= 10
    first_digit, second_digit = double_of_digit.to_s.split('')
    sum_of_digits = first_digit.to_i + second_digit.to_i
    return sum_of_digits.to_s
  else
    return double_of_digit.to_s
  end
end

def card_checksum(number)
  checksum = 0

  number.split('').each do |digit|
    checksum += digit.to_i
  end

  checksum % 10 == 0 ? true : false
end

def card_is_valid?(card_number)
  card_number = card_number.tr(' ', '')

  card_check = ''

  card_number.reverse.split('').each_with_index do |digit, index|
    if (index + 1) % 2 == 0
      card_check += check_digit(digit.to_i)
    else
      card_check += digit
    end
  end

  checksum = card_checksum(card_check.reverse)

  return checksum ? 1 : 0
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    puts card_is_valid?(line.chomp)
  end
end
