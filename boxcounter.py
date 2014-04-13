import Image

def to2dArray(im):
	array2 = []
	for i in range(image.size[0]):
		array = []
		for j in range(image.size[1]):
			if image.getpixel((i, j)) != (255, 255, 255):
				array = array + [1]
			else:
				array = array + [0]
		array2 = array2 + [array];
	return array2

def completeBox(image, x, y, width, height):
	for i in range(x, x+width):
		if image[i][y] != 1:
			return False
	for j in range(y-height, y):
		if image[x][j] != 1:
			return False
	print x, '\t', y-height, '\t', width, '\t', height, '\t'
	return True

def tryBoxes2(image, x, y, width):
	boxes = 0;
	for j in range(y+1, len(image[0])):
		if image[x][j] != 1:
			break
		if image[x-1][j] == 1 and completeBox(image, x-width, j, width, j-y):
			boxes = boxes + 1
	return boxes

def tryBoxes1(image, x, y):
	boxes = 0;
	for i in range(x+1, len(image)):
		if image[i][y] != 1:
			break
		if image[i][y+1] == 1:
			boxes = boxes + tryBoxes2(image, i, y, i-x)
	return boxes

def countBoxes(image):
	boxes = 0;
	for j in range(len(image[0])):
		for i in range(len(image)):
			if i < len(image)-1 and j < len(image[0])-1 and image[i][j] == 1:
				if image[i+1][j] == 1 and image[i][j+1] == 1:
					boxes = boxes + tryBoxes1(image, i, j)
	return boxes;

image = Image.open('boxes.png')
image = image.convert('RGB')
image = to2dArray(image)

print 'X\tY\tWidth\tHeight'
print countBoxes(image), 'boxes';
