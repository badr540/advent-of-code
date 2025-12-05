import os
import time
from PIL import Image
import numpy as np

def calculate_entropy(image):
    # Open the image and convert to grayscale
    pixel_values = np.array(image)

    # Create a histogram of pixel intensities
    histogram, _ = np.histogram(pixel_values, bins=256, range=(0, 256))

    # Normalize the histogram to get probabilities
    probabilities = histogram / histogram.sum()

    # Calculate the entropy
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))  # Add small epsilon to avoid log(0)
    return entropy

height = 103
width = 101

def predict_robot_movements(pos,vel,h,w,seconds):
    for i in range(seconds):
        pos[0] = (pos[0] + vel[0])%w
        pos[1] = (pos[1] + vel[1])%h
    
    return pos
total = 0
positions = []
velocities = []

filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        positions.append(line.split(" ")[0].split("=")[1].split(','))
        velocities.append(line.split(" ")[1].rstrip('\n').split("=")[1].split(','))
        for i in range(2):
            positions[len(positions)-1][i] = int(positions[len(positions)-1][i])
            velocities[len(velocities)-1][i] = int(velocities[len(velocities)-1][i])




    
start = time.time()
total_entropy = 0
average_entropy = 0
lowest_entropy = 1
for s in range(1,100000):
    image = Image.new("L", (width, height)) 
    for i in range(len(positions)):
        x,y = predict_robot_movements(positions[i], velocities[i], height,width,1)

        
        image.putpixel((x, y), 255)
        
    entropy = calculate_entropy(image)
    if entropy < average_entropy*0.95:
        image.save("binary_list_image_{}.png".format(s))
    if entropy < lowest_entropy:
        lowest_entropy = entropy
        image.save("binary_list_image_{}.png".format(s))
        
    total_entropy += entropy
    average_entropy = total_entropy/(s)
    

quadrants = [ [[0,0], [int(height/2), int(width/2)]], 
             [[0,int(width/2)+1], [int(height/2), width]],
             [[int(height/2)+1,0], [height, int(width/2)]], 
             [[int(height/2)+1,int(width/2)+1], [height, width]]
            ]
quadrants_scores = []
quad_idx = -1

for quad in quadrants:
    quad_idx += 1
    quadrants_scores.append(0)
    for y in range(quad[0][0], quad[1][0]):
        for x in range(quad[0][1], quad[1][1]):
            if map[y][x].isdigit():
                quadrants_scores[quad_idx] += int(map[y][x]) 


saftey_factor = 1
for q in quadrants_scores:
    saftey_factor *= q

print(saftey_factor)    
end = time.time()
print(end - start)