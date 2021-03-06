import os
from propagation import Propagator

workdir = "/users/jileihao/playground/sandbox"

# Create a new Propagator
p = Propagator()

# bavcta001
# fnimg = os.path.join(workdir,"test/img4d__bavcta001_trim.nii.gz")
# fnseg = os.path.join(workdir, "test/seg03_bavcta001_trim.nii.gz")
# fref = 3
# targetFrame = [1,3,7]

# bav07
fnimg = os.path.join(workdir, "test/bav07_dcm/bav07.dcm")
fnseg = os.path.join(workdir, "test/bav07_dcm/seg05_bav07_root_labeled_LPS.nii.gz")
fref = 5
targetFrame = [3,5]

# Set Parameters
p.SetTag("dev")
p.SetInputImage(fnimg)
p.SetReferenceSegmentation(fnseg)
p.SetReferenceFrameNumber(fref)
p.SetGreedyLocation(os.path.join(workdir, "greedy"))
p.SetVtkLevelSetLocation(os.path.join(workdir, "vtklevelset"))
p.SetTargetFrames(targetFrame)
p.SetOutputDir(os.path.join(workdir, "out"))

# Run propagation
p.Run()