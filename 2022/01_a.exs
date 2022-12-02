# get input data as blocks separated by empty lines
Utils.get_input_blocks
# convert each value in block to integer and sum
|> Stream.map(fn items -> Enum.map(items, &String.to_integer/1) |> Enum.sum end)
# select largest calorie value
|> Enum.reduce(fn next_cal, best_cal -> max(next_cal, best_cal) end)
# print result
|> IO.inspect()
