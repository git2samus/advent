defmodule Main do
  def self_score("X"), do: 1
  def self_score("Y"), do: 2
  def self_score("Z"), do: 3

  def match_score(opponent, self) do
    # convert to bitstring to extract numeric char values
    {<<o_bs>>, <<s_bs>>} = {opponent, self}

    # "ABC" and "XYZ" are consecutive values, difference mod 3 is constant
    case rem(s_bs-o_bs, 3) do
      0 -> 6 # win
      1 -> 0 # lose
      2 -> 3 # draw
    end
  end

  def calc_score([opponent, self]) do
    match_score(opponent, self) + self_score(self)
  end
end

Utils.get_input_tokens
|> Stream.map(&Main.calc_score/1)
|> Enum.sum
|> IO.inspect
