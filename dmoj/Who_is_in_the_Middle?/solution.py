# https://dmoj.ca/problem/ccc07j1

first_weight = int(input())
second_weight = int(input())
third_weight = int(input())

if ((first_weight >= second_weight and first_weight <= third_weight)
   or (first_weight <= second_weight and first_weight >= third_weight)):
    m_bowl = first_weight

if ((second_weight >= first_weight and second_weight <= third_weight)
   or (second_weight <= first_weight and second_weight >= third_weight)):
    m_bowl = second_weight

if ((third_weight >= first_weight and third_weight <= second_weight)
   or (third_weight <= first_weight and third_weight >= second_weight)):
    m_bowl = third_weight

print(m_bowl)
