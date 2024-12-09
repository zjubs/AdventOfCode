with open('2024/Day9/Day9Input.txt', 'r') as f:
    puzzle = f.read()


lengths = [int(num) for num in puzzle]

blocks = {} # id: [pos,len]
gaps = {} # len:[position]
pos = 0
id =0 
for i,file_len in enumerate(lengths):
    if  i % 2 == 0:
        blocks[id] = [pos, file_len]
        id+=1
    else:
        update = gaps.get(file_len,[])
        update.append(pos)
        gaps[file_len] = update

    pos += file_len

rev_blocks = sorted(blocks.keys(),reverse=True)
for i in rev_blocks:
    file_start_pos,file_len = blocks[i]
    possible_gaps = sorted([[gaps[gap_len][0],gap_len] for gap_len in gaps if gap_len>=file_len])
    if possible_gaps:
        # find first suitable gap
        gap_start_pos,gap_len = possible_gaps[0]
        if file_start_pos > gap_start_pos:
            blocks[i] = [gap_start_pos,file_len]
            gap_remaining = gap_len - file_len
            # update list of gaps gap_len
            update = gaps[gap_len]
            del update[0]
            gaps[gap_len] = sorted(update)

            if gap_remaining:
                # update list of gaps of remaining length
                update = gaps.get(gap_remaining,[])
                update.append(gap_start_pos+file_len)
                gaps[gap_remaining] = sorted(update)

#calc checksum
part2 = 0
for id,(start,length) in blocks.items():
    for i in range(length):
        part2 += id*(start+ i)



print(part2) #6221662795602
x = 1