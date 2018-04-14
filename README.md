# batch-resize
Python script to resize every image in a folder to a specified size.

# Arguments
<pre>
-h or -help
	- List arguments and their meanings
-s or -size
	- New pixel value of both width and height.
-x or -width
	- New pixel value of width
-y or -height
	- New pixel value of height
-t or -scale
	- Scales pixel sizes
</pre>
<hr/>

# Example Usage
<pre>
python batch_resize.py -d folder_name -s 128
-> Resizes all images in 'folder_name' to 128x128px

python batch_resize.py -d full/path/to/image_folder -x 128 -y 256
-> Resizes all images in 'image_folder' (listed as a full path, do this if you're not in the current working directory) to 128x256px

python batch_resize.py -d folder_name -t 2
-> Resizes all images in 'folder_name' to twice their original size
</pre>
<hr />

## Accepted Image Types:
<pre>
- Jpg, Png, Bmp (more can easily be added by editing the 'accepted_types' list in the python file)
</pre>
<hr />

# Dependencies
<pre>
- Pillow, a fork of PIL.
  - Download from pip:
    - pip install Pillow
  - Link to their Github:
    - https://github.com/python-pillow/Pillow
</pre>
