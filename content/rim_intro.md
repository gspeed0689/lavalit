# Details of Capturing the Data of the Caldera Cliff

The lit area of the caldera cliff face was captured with my Fuji X-T50 with the Tamron 17-70 f/2.8 at 70mm. 
Each image was shot at 1/250 s, the aperture was set to auto and ranged from f/4 to f/10, and the ISO was also set to auto and was either 125 or 160. 
The images were processed in Lightroom Classic to enforce a consistent white balance, and were exported to full resolution jpegs. 

The photos were processed in Agisoft Metashape Standard 1.7. 
All photos were aligned, and used for creating the dense point cloud. 
The dense point cloud is 211 million points, and most of the sky was removed using the select points by color tool. 
The size of the point cloud is too prohibitive to convert to a mesh, so one has not been generated.

I found LiDAR derived digital elevation model (DEM) data for Vesuvius, I converted the raster to a point cloud in QGIS. 
I brought the point cloud into CloudCompare, and used the alignment tools to georeference my photogrammetry model to the georeferenced LiDAR derived data. 

![Georeferenced view of the LiDAR derived data in white, and my generated point cloud in color.](https://garrettspeed.com/wp-content/uploads/2025/01/caldera-ptcloud-03-scaled.webp)

The georeferenced model is not found in this web tool, as the precision of the floating point numbers of the points in the clouds was not correct, so data precision has been lost. 
In the screenshot below the data should be regular and flat contours:

![Screenshot of the georeferenced point cloud and the countouring that should not be occuring. ](https://garrettspeed.com/wp-content/uploads/2025/01/precision-loss-scaled.webp)

The alignment of the photos in the photogrammetry software was used to create the groupings of the photos for the panoramas. 
The low and high image numbers were used to create a table of images included in each panorama. 
For highest bit-depth, the images were exported from Lightroom to 16-bit TIFs. 
The individual images were processed with Microsoft Image Composite Editor (ICE), which does a fantastic job of stitching panoramas together when the photos were not strictly shot with the same nodal point. 
Using my photo table and Python, I auto generated Image Composite Editor files to streamline the GUI processing workflow. 

I used the OSM Tracker for Android app to collect a GNSS (GPS) point once a second, this app exported each point with a time stamp and a latitude and longitude in a GPX file. 
I captured a photo of `time.gov` and calculated the offset of the camera time to UTC. 
I loaded the capture times of the photos into a table, and using the first and last images in each panorama, took all of the GNSS points in that time frame, and averaged the points in that time frame to what is theoretically a more precise location for each panorama. 
The panorama locations can be seen in the map below: