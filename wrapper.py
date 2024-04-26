import sys

import subprocess
from subprocess import call


from biaflows.helpers import BiaflowsJob

# Assuming biom3d has relevant classes/functions you need to import


def main(argv):
    
    with BiaflowsJob.from_cli(argv) as bj:
  


        img_dir = bj.parameters.img_dir
        img_dir = bj.parameters.msk_dir
        num_classes = bj.parameters.num_classes
        description = bj.parameters.desc
        
 
        # Construct the command to run biom3d
        cmd = [
            "source", "b3d/bin/activate",
            "&&", "python", "-m", "biom3d.preprocess_train",
            "--img_dir", img_dir,
            "--msk_dir", img_dir,
            "--num_classes", str(num_classes),
            "--desc", description,
            "&&", "deactivate"
        ]


        status = subprocess.run(cmd)

        if status.returncode != 0:
            print("Running Biom3d failed, terminate")
            sys.exit(1)
                # 5. Pipeline finished

        

if __name__ == "__main__":
    main(sys.argv[1:])
