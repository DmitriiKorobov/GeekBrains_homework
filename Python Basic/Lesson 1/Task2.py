cube = list(range(1, 1000, 2))
answer_1 = 0
answer_2 = 0

for i in range(len(cube)):
    cube[i] = cube[i]**3
    element_cube = cube[i]
    element_cube_sum = cube[i]
    segment_sum = 0

    while element_cube > 0:
        segment_element_cube = element_cube % 10
        segment_sum = segment_sum + segment_element_cube
        element_cube = element_cube // 10
        segment_sum_div = segment_sum / 7
    else:
        if segment_sum_div * 10 == int(segment_sum_div) * 10:
            answer_1 = answer_1 + element_cube_sum
print('Answer on task 2 part "a" =', answer_1)

for i in range(len(cube)):
    element_cube_part2 = cube[i] + 17
    element_cube_sum_part2 = cube[i] + 17
    segment_sum_part2 = 0

    while element_cube_part2 > 0:
        segment_element_cube = element_cube_part2 % 10
        segment_sum_part2 = segment_sum_part2 + segment_element_cube
        element_cube_part2 = element_cube_part2 // 10
        segment_sum_div = segment_sum_part2 / 7
    else:
        if segment_sum_div * 10 == int(segment_sum_div) * 10:
            answer_2 = answer_2 + element_cube_sum_part2
print('Answer on task 2 part "b" =', answer_2)
print('The list has NOT changed\n', cube, sep='')
