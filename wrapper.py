import sys
import os
from subprocess import call
# Assuming biom3d has relevant classes/functions you need to import
from biom3d import preprocess_train, other_necessary_functions

def prepare_data():
    # Assuming these environment variables are set correctly
    img_dir = os.getenv("IMG_DIR")
    msk_dir = os.getenv("MSK_DIR")
    num_classes = int(os.getenv("NUM_CLASSES"))
    description = os.getenv("DESCRIPTION")
    return img_dir, msk_dir, num_classes, description
    
def run_biom3d_workflow(img_dir, msk_dir, num_classes, description):
    # Construct the command to run biom3d
    command = [
        "python", "-m", "biom3d.preprocess_train",
        "--img_dir", img_dir,
        "--msk_dir", msk_dir,
        "--num_classes", str(num_classes),
        "--desc", description
    ]
    return_code = call(command, shell=True)
    if return_code != 0:
        raise ValueError(f"Failed to execute biom3d with return code: {return_code}")

def main(argv):
    try:
        # Get data paths and parameters from environment variables
        img_dir, msk_dir, num_classes, description = prepare_data()

        # Run the biom3d training process
        run_biom3d_workflow(img_dir, msk_dir, num_classes, description)

        print("Workflow completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main(sys.argv[1:])
