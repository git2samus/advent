#!/usr/bin/env elixir

defmodule Main do
  @numbers_pattern "one|two|three|four|five|six|seven|eight|nine"

  defp replace_spelled("one"), do: "1"
  defp replace_spelled("two"), do: "2"
  defp replace_spelled("three"), do: "3"
  defp replace_spelled("four"), do: "4"
  defp replace_spelled("five"), do: "5"
  defp replace_spelled("six"), do: "6"
  defp replace_spelled("seven"), do: "7"
  defp replace_spelled("eight"), do: "8"
  defp replace_spelled("nine"), do: "9"
  defp replace_spelled(digit), do: digit

  defp extract_first(line, numbers_pattern \\ @numbers_pattern) do
    numbers_re = ~r/#{numbers_pattern}|[0-9]/
    Regex.run(numbers_re, line, capture: :first) |> hd
  end

  defp extract_last(line) do
    extract_first(String.reverse(line), String.reverse(@numbers_pattern)) |> String.reverse
  end

  def process_line(line) do
    # extract first and last number/digit, replace spelled number with digit
    [first, last] = [extract_first(line), extract_last(line)] |> Enum.map(&replace_spelled/1)
    # concat first and last digit, convert to integer
    first <> last |> String.to_integer
  end
end


## begin program ##

# read input from stdin
IO.stream
# convert each line to the required number
|> Enum.map(&Main.process_line/1)
# sum converted lines
|> Enum.sum
# print result
|> IO.inspect
