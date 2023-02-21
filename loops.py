
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():
    shape = input("Please enter Shape: ").lower()
    return shape


# TODO: Step 1 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    height = int(input("Please enter Height: "))

    while height > 80:
        height = input("Please enter Height: ")
    else:
        return height


# TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    for i in range (height):
        print(f"*"*height)

def draw_triangle_reversed(height):
    for i in range(height,0,-1):
        print((str(height-(i-1))+" ")*i,end="\n")

def draw_triangle(height):
    
    for i in range(0,height+1):
        print((str(j)+" ")*i,end="\n")

    

def draw_triangle_multiplication(height):
    for i in range(1,(height+1)):
        i = i*i
        print((str(i)+" ")*height,end="\n")
        height = height -1
        

def draw_pyramid(height):
    space = height-1
    for i in range(1,(height*2),2):
        print(" "*(space)+"*"*i)
        space = space-1
        
       
def draw_triangle_prime(height):
    pass
         
                
# TODO: 4 - add support for other shapes
def draw(shape, height):
    if shape == "square":
        draw_square(height)
    elif shape == "triangle":
        draw_triangle(height)
    elif shape == "pyramid":
        draw_pyramid(height)
    elif shape == "triangle reversed":
        draw_triangle_reversed(height)
    elif shape == "triangle multiplication":
        draw_triangle_multiplication(height)
    elif shape == "triangle prime":
        draw_triangle_prime(height)



if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)