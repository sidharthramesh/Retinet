#/bin/bash
echo "Converting..."
python csvpath.py &
python convert.py --crop_size 512 --convert_directory test_resized/ --extension jpeg --directory test/
python csvpath.py &
echo "Opening notebook..."
jupyter-notebook notebooks/Sample_prediction.ipynb 

