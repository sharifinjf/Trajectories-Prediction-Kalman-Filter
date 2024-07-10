<p align="center">
<img src="/Images/Sample.png" alt="Alt text" width="800" height="600"/>
</p>
<p align="center">
<img src="/Images/Demo.gif" alt="Alt text" width="800" height="600"/>
</p>

Blue: Represents the past trajectory of the object <br>
Green: Indicates the ground truth path the object followed<br>
Red: Shows the predicted future trajectory based on the model<br>

# Trajectory Prediction Project
## Overview
This project focuses on trajectory prediction using various models. It leverages the KITTI dataset for training and evaluation and provides tools for visualizing the predicted trajectories.

The codes are based on codes of the trajectory prediction shared by https://github.com/fedebecat and is modified to address our desired goals.

# Setup
## Create a Virtual Environment
To ensure the correct dependencies are installed, it's recommended to create a virtual environment. Run the following commands:<br>
`python -m venv env`<br>
`source env/bin/activate`   # On Windows use `env\Scripts\activate`<br>
## Install Dependencies
Install the necessary Python packages using pip:<br>
`pip install -r requirements.txt`<br>
## Dataset 
### Download KITTI Dataset
First, download the KITTI Raw dataset and split it into the appropriate format. Place the dataset in the kitti_raw_data folder.
## Training and Evaluation
To run and evaluate your model, run the main.py script. 

### Run the script using:
`python main.py`
## Plotting Trajectories
To visualize the predicted trajectories, run the plot_trajectory.py script:<br>
`python plot_trajectory.py`<br>

# Contributions
Contributions are welcome! Please feel free to submit a Pull Request or open an issue.
