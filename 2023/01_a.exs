#!/usr/bin/env elixir

defmodule Main do
  def process_line(line) do
    # remove non-digits from line
    digits = String.replace(line, ~r/[^0-9]/, "")
    # concat first and last digit, convert to integer
    String.first(digits) <> String.last(digits) |> String.to_integer
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
