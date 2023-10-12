def print_slide(slide):
    print('\n'.join(slide))
    print('---')

prev_slide = []

slide = []
rowi = -1
eq = True
while True:
    rowi += 1
    row = input()
    if row == 'KONIEC':
        print_slide(prev_slide)
        print('KONIEC')
        break

    if row == '---':
        if len(prev_slide) > len(slide) or not eq:
            print_slide(prev_slide)
        prev_slide = slide
        slide = []
        rowi = -1
        eq = True
        continue

    slide.append(row)
    if rowi < len(prev_slide):
        eq = eq and (prev_slide[rowi] == slide[rowi])
