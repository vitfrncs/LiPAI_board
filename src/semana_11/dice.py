import numpy as np

def dice(mask_pred, mask_gt):
    mask_pred = mask_pred.astype(bool)
    mask_gt = mask_gt.astype(bool)

    inter = np.logical_and(mask_pred, mask_gt).sum()
    total = mask_pred.sum() + mask_gt.sum()

    if total == 0:
        return 1.0
    return 2 * inter / total