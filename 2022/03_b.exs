defmodule Main do
  defp get_map(line) do
    # convert string to list of characters
    String.graphemes(line)
    # create MapSet from list of characters
    |> MapSet.new
  end

  def find_common(lines) do
    # create MapSet from each line
    Enum.map(lines, &get_map/1)
    # get repeated characters from both sets
    |> Enum.reduce(&MapSet.intersection(&1, &2))
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
|> Stream.chunk_every(3)
|> Stream.map(&Main.find_common/1)
|> Stream.map(&Main.get_priority/1)
|> Enum.reduce(&(&1 + &2))
|> IO.inspect
