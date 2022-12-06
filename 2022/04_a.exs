defmodule Main do
  def parse_line(line) do
    String.split(line, ",")
    |> Enum.map(&String.split(&1, "-"))
    |> Enum.map(fn
      items -> Enum.map(items, &String.to_integer/1)
    end)
  end

  def count_overlaps([[l1, r1], [l2, r2]]) do
    if (l1 <= l2 && r1 >= r2) || (l2 <= l1 && r2 >= r1) do
      1
    else
      0
    end
  end
end

Utils.get_input
|> Stream.map(&Main.parse_line/1)
|> Stream.map(&Main.count_overlaps/1)
|> Enum.sum
|> IO.inspect
