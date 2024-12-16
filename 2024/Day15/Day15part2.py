
class Box:
    def __init__(self, left:tuple):
        self.pos = (left,self._add_tuple(left, (0,1)))
        self.moves = {
            '^': (-1,0),
            '>': (0,1),
            '<': (0,-1),
            'v': (1,0)}
        
     # Implementing __hash__ and __eq__ to make Box instances hashable
    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return id(self) == id(other)
        
    @staticmethod
    def _add_tuple(tuple1:tuple,tuple2: tuple):
        return tuple(a + b for a, b in zip(tuple1, tuple2))
    
    
    def contains_any_position(self, position: tuple) -> bool:
        #Check if the box contains a specified position
        return any(pos == position for pos in self.pos)
    
    def contains_any_position_box(self, pushed_box_pos: set) -> bool:
        #Check if the box contains any of the specified positions
        return any(pos == position for pos in self.pos for position in pushed_box_pos)

    def potential_move(self,dir: str):
        # get potential postion of box
        move = self.moves[dir]
        return (self._add_tuple(self.pos[0], move),self._add_tuple(self.pos[1], move))
    
    def move(self,dir: str):
        #move box to new position
        self.pos = self.potential_move(dir)

    def push(self,boxes: set ,grid: dict,dir: str):
        # use try push to check if can push boxes and get depndent boxes
        # then move each box
        can_push,push_boxes = self.try_push(boxes -{self},grid,dir)

        if can_push:
            push_boxes.add(self)
            for box in push_boxes:
                box.move(dir)
            return True
        else:
            return False
    
    def try_push(self,other_boxes: set ,grid: dict,dir: str):
        # check if can push a box and get all dependent boxes
        can_push = True
        new_pos = self.potential_move(dir)
        other_boxes = boxes - {self}
        
        boxes_in_way = set(
            box for box in other_boxes if box.contains_any_position_box(new_pos)
        )
        all_child_boxes = boxes_in_way
        if grid[new_pos[0]] == '#' or grid[new_pos[1]] == '#':
            can_push = False
        elif boxes_in_way:
            for box in boxes_in_way:
                possible,child_boxes = box.try_push(other_boxes - {self},grid,dir)
                all_child_boxes = all_child_boxes | child_boxes
                if not possible:
                    can_push = False
             
        return can_push, all_child_boxes

with open('2024/Day15/Day15Input.txt', 'r') as f:
    puzzle = f.read()

g,m = puzzle.split('\n\n')
g = g.split('\n')

# prep instructions
instructions = ''.join(m.split('\n'))

# prep grid
grid = {}
boxes = set()
for i,line in enumerate(g):
    for j,chr in enumerate(line):

        if chr == '@':
            curr = (i,j*2)
            grid[(i,j*2)] = '.'
            grid[(i,j*2+1)] = '.'
        
        elif chr == 'O':
            grid[(i,j*2)] = '.'
            grid[(i,j*2+1)] = '.'
            box = Box((i,j*2))
            boxes.add(box)

      
        else: # # and .
            grid[(i,j*2)] = chr
            grid[(i,j*2+1)] = chr

def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))

moves = {
    '^': (-1,0),
    '>': (0,1),
    '<': (0,-1),
    'v': (1,0)}

for num,dir in enumerate(instructions):

    proposed = add_tuple(curr,moves[dir])

    proposed_boxes = [box for box in boxes if box.contains_any_position(proposed)]

    if grid[proposed] == '#':
        curr = curr

    elif grid[proposed] == '.' and not proposed_boxes:
        curr = proposed
    else:
        # pushing boxes
        move = proposed_boxes[0].push(boxes,grid,dir)
        if move:
            curr = proposed

part2 = 0
for box in boxes:
    coords = box.pos[0]
    part2 += 100* coords[0] + coords[1]

print(f'part2:{part2}')

