defmodule Main do
  def split_line(line) do
    # split line at half length
    String.split_at(line, div(String.length(line), 2))
  end

  def find_difference(line_halfs) do
    # convert Tuple to List to get Enumerable
    Tuple.to_list(line_halfs)
    # convert each string to list of characters
    |> Enum.map(&String.graphemes/1)
    # create MapSet from list of characters
    |> Enum.map(&MapSet.new/1)
    # get repeated characters from both sets
    |> then(fn [left, right] -> MapSet.intersection(left, right) end)
    # convert to list to get head
    |> MapSet.to_list
    # get only element in list
    |> hd
  end

  def get_priority(item_type) do
    # a-z is code 97-122, A-Z is code 65-90
    <<item_code>> = item_type

    if item_code >= 97 do
      item_code - 96
    else
      item_code - 38
    end
  end
end

Utils.get_input
|> Stream.map(&Main.split_line/1)
|> Stream.map(&Main.find_difference/1)
|> Stream.map(&Main.get_priority/1)
|> Enum.reduce(&(&1 + &2))
|> IO.inspect
