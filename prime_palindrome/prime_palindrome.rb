biggest_prime_palindrome = 0

def is_prime?(number)
  number_minus_one = number - 1
  number_minus_one.downto(2) do |divisor|
    if number % divisor == 0
      return false
    end
  end

  true
end

def is_palindrome?(number)
  number_string = number.to_s

  number_string == number_string.reverse ? true : false
end

(1..1000).each do |number|
  if is_prime?(number) and is_palindrome?(number)
    biggest_prime_palindrome = number
  end
end

puts biggest_prime_palindrome
