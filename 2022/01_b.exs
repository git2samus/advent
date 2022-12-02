defmodule Main do
  def compact_chunk(items) do
    # convert each value in block to integer and sum
    Enum.map(items, &String.to_integer/1) |> Enum.sum
  end

  def best_three(next_cal, acc_cals) do
    case acc_cals do
      [] ->
        # init accumulator
        [next_cal]
      _ ->
        # prepend new value to calories accumulator, sort by largest and take first three
        Enum.sort([next_cal | acc_cals], :desc) |> Enum.take(3)
    end
  end
end

# get input data as blocks separated by empty lines
Utils.get_input_blocks
# convert each value in block to integer and sum
|> Stream.map(&Main.compact_chunk/1)
# select largest calorie value
|> Enum.reduce([], &Main.best_three/2)
# sum best three
|> Enum.sum
# print result
|> IO.inspect()
