# Image Types:

# 1- Binary Images : m by n array of Pixels just have two values 0(black) or 1(white) or vise versa;
# 2- GrayScale Images: m by n array of pixels have values:
# uint8 : [0:255] , uint16: [0:62535] and so on;
# 3- TrueColor RGB : m by n by 3 array of pixels each array pixels have values like GrayScale represents red , green or blue depending on array
# 4- Indexed Image: pixels are direct indices into colormap m by 3 array for RGB 

# Conver between Types of Images functions;
# im2bw | gray2ind() , ind2gray() , mat2gray(), rgb2gray() | ind2rgb() , rgb2ind() | label2rgb()

# To Detect Round Shapes
 
# Conversion To Binary Image:
 
# 1- Read Image
rgb = imread('../Images/RoundImage.png');
# 2- Convert From RGB To Gray Deal With One Matrix Pixels Image (One Channel)
gray = rgb2gray(rgb);
# 3- Get threshold of image to be able to detect pixel is one or zero when converting to binary.
threshold = graythresh(gray);
# 4- Conversion To Binary
binary = im2bw(gray,threshold); 
# 5- Another Way To Convert To Binary Using Edges
edged = edge(gray,'canny'); # acctuly edge function do all of this but need just grayscale


# Remove Noise 

# 1- remove all objects fewer than 30 pixels
binaryRemoveObjects = bwareaopen(binary,30);

# 2- fill the gap in the pen's cap
se = strel('square',2); # disk is shape to  fill gap in matlab but here is square or diamond
binaryFilledGap = imclose(binaryRemoveObjects,se);

# 3- fill any holes
binaryFilledHoles = imfill(binaryFilledGap,'holes');


# Find Boundaries : Exclude Image with Two methods Boundaries and Labels;
[B,L] = bwboundaries(binaryFilledHoles,8);  

#noholes in matlab but here is 8 or 4
# B List of boundaries for each shape for example B[1] is a matrix N X 2(cause it's 2D Image each Boundary pixel is (X,Y) just)
# L Label Image (Instead of giving pixels values of color , gives them Position values (Ex : 0 for background) 

# For Debuggin And Testing if Boundaries is Applied on Shapes or not
#imshow(label2rgb(L,@hsv,[.5 .5 .5]));
#hold on
#for i=1:length(B)
#   boundary = B{i};
#   plot(boundary(:,2), boundary(:,1), 'w', 'LineWidth', 2);
#end

# Find Round Shapes => Law of Roundness : metric = 4*pi*area/perimeter^2.

stats = regionprops(L,'Area','Centroid','BoundingBox');
# loop over the boundaries
for k = 1:length(B)
# obtain (X,Y) boundary coordinates corresponding to label 'k'
boundary = B{k};
# compute a simple estimate of the object's perimeter
delta_sq = diff(boundary).^2;
perimeter = sum(sqrt(sum(delta_sq,2)));
# obtain the area calculation corresponding to label 'k'
area = stats(k).Area;
# compute the roundness metric
metric = 4*pi*area/perimeter^2;
# display the results
metric_string = sprintf('%2.2f',metric);
# mark objects above the threshold with a black circle
if metric > 0.9
centroid = stats(k).Centroid;
plot(centroid(1),centroid(2),'ko'); bbox=stats(k).BoundingBox;
rectangle('Position', [bbox(1)-5,bbox(2)-5,bbox(3)+15,bbox(4)+15],...
'EdgeColor','r','LineWidth',2 )
end
text(boundary(1,1)-35,boundary(1,1)+13,metric_string,'Color','y',...
'FontSize',14,'FontWeight','bold');
end
title(['Metrics closer to 1 indicate that the object is approximately round'])
