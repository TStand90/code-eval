<?php

function fizzbuzz($fizz, $buzz, $count)
{
    $result = "";

    for ($i = 1; $i <= $count; $i++)
	{
		if ($i % $fizz == 0 && $i % $buzz == 0)
		{
            $result .= "FB ";
		}
		elseif ($i % $fizz == 0)
		{
            $result .= "F ";
		}
		elseif ($i % $buzz == 0)
		{
            $result .= "B ";
		}
		else
		{
            $result .= "$i ";
		}

	}

	$result = trim($result);

	return $result;
}

$fh = fopen($argv[1], "r");

while (!feof($fh))
{
  $test = trim(fgets($fh));

  if ($test != "")
  {
    $file_data = explode(" ", $test);

    $fizz = $file_data[0];
    $buzz = $file_data[1];
    $count = $file_data[2];

	$result = fizzbuzz($fizz, $buzz, $count);

	echo $result . "\n";
  }
}
?>
