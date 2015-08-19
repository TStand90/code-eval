ENCODING = {
  "1" => "A", "2" => "B", "3" => "C", "4" => "D", "5" => "E", "6" => "F", "7" => "G",
  "8" => "H", "9" => "I", "10" => "J", "11" => "K", "12" => "L", "13" => "M", "14" => "N",
  "15" => "O", "16" => "P", "17" => "Q", "18" => "R", "19" => "S", "20" => "T", "21" => "U",
  "22" => "V", "23" => "W", "24" => "X", "25" => "Y", "26" => "Z"
}

def decode_number(number)
  number_of_decodings = 0
  number.split("").each do |digit|
    if ENCODING.has_key?(digit)
      number_of_decodings += 1
      break
    end
  end
  
  return number_of_decodings
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    puts decode_number(line.chomp)
  end
end
