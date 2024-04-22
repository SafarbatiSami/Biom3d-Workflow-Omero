import sys

import subprocess
from subprocess import call

from biaflows import CLASS_OBJSEG, CLASS_SPTCNT, CLASS_PIXCLA, CLASS_TRETRC, CLASS_LOOTRC, CLASS_OBJDET, CLASS_PRTTRK, CLASS_OBJTRK
from biaflows.helpers import BiaflowsJob, prepare_data, upload_data, upload_metrics, get_discipline

# Assuming biom3d has relevant classes/functions you need to import


def main(argv):
    
    with BiaflowsJob.from_cli(argv) as bj:
        # Change following to the actual problem class of the workflow
        problem_cls = get_discipline(bj, default=CLASS_OBJSEG)
        # 1. Prepare data for workflow
        in_imgs, gt_imgs, in_path, gt_path, out_path, tmp_path = prepare_data(problem_cls, bj, is_2d=False, **bj.flags)

        # 2. Run image analysis workflow
        bj.job.update(progress=25, statusComment="Launching workflow...")
        # Assuming these environment variables are set correctly
        img_dir = bj.parameters.img_dir
        img_dir = bj.parameters.msk_dir
        num_classes = bj.parameters.num_classes
        description = bj.parameters.desc
        
 
        # Construct the command to run biom3d
        cmd = [
            "python", "-m", "biom3d.preprocess_train",
            "--img_dir", img_dir,
            "--msk_dir", img_dir,
            "--num_classes", str(num_classes),
            "--desc", description
        ]


        status = subprocess.run(cmd)

        if status.returncode != 0:
            print("Running Biom3d failed, terminate")
            sys.exit(1)
                # 5. Pipeline finished

        

if __name__ == "__main__":
    main(sys.argv[1:])
