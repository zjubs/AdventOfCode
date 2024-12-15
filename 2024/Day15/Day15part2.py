
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
        return hash(self.pos)  # Use the position as the hash

    def __eq__(self, other):
        return isinstance(other, Box) and self.pos == other.pos
        
    @staticmethod
    def _add_tuple(tuple1:tuple,tuple2: tuple):
        return tuple(a + b for a, b in zip(tuple1, tuple2))
    
    # def contains_position(self, position: tuple) -> bool:
    #     """Check if a given position is part of this box."""
    #     return position in self.pos
    
    def contains_any_position(self, positions: set) -> bool:
        """Check if the box contains any of the specified positions."""
        return any(pos in self.pos for pos in positions)

    def potential_move(self,dir):
        # get potential postion of box
        move = self.moves[dir]
        return (self._add_tuple(self.pos[0], move),self._add_tuple(self.pos[1], move))
    
    def move(self,dir):
        #move box to new position
        self.pos = self.potential_move(dir)



    
    def push(self,boxes: set ,grid: dict,dir: str):
        can_push,push_boxes = self.try_push(boxes,grid,dir)

        if can_push:
            push_boxes.add(self)
            for box in push_boxes:
                box.move(dir)
            return True
        else:
            return False
        




    
    def try_push(self,boxes: set ,grid: dict,dir: str):
        can_push = True
        new_pos = self.potential_move
        (dir)
        other_boxes = boxes - {self}
        
        boxes_in_way = set(
            box for box in other_boxes if box.contains_any_position(new_pos)
        )
        all_child_boxes = boxes_in_way
        if grid[new_pos[0]] == '#' or grid[new_pos[1]] == '#':
            can_push = False
        elif boxes_in_way:
            for box in boxes_in_way:
                possible,child_boxes = box.try_push(other_boxes,grid,dir)
                all_child_boxes = all_child_boxes | child_boxes
                if not possible:
                    can_push = False
             
        return can_push, all_child_boxes
    # need to store all boxes pushed if possible and if they can be pushed
    #if can push then move them all
    #if can't push then don't move them
        



with open('2024/Day15/Day15Sample3.txt', 'r') as f:
    puzzle = f.read()

g,m = puzzle.split('\n\n')
g = g.split('\n')

# prep instructions
instructions = ''.join(m.split('\n'))

# prep grid
grid = {}
boxes = set()
box_num = 0
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

for dir in instructions:
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


# box1 = Box((0,1))
# box2 = Box((3,2))

# boxes = set()
# boxes.add(box1)
# boxes.add(box2)

# box1.push(boxes,grid,'>')

# box1.move_to('>')

x = 1





# x = 1



# moves = {
#     '^': (-1,0),
#     '>': (0,1),
#     '<': (0,-1),
#     'v': (1,0)}