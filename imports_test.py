try:
    import tensorflow
    import keras
    import cv2
    import numpy
    import matplotlib
    import h5py
    import scipy
except Exception as import_error:
    raise ImportError(f"{str(import_error)}")


if __name__ == "__main__":
    assert tensorflow
    assert cv2
    assert numpy
    assert matplotlib
    assert h5py
    assert keras
    assert scipy
