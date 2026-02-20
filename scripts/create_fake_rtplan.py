from pydicom.dataset import Dataset, FileDataset
import datetime
import os

# -----------------------------
# File path
# -----------------------------
filename = "../data/sample_rtplan.dcm"

# -----------------------------
# Create basic DICOM metadata
# -----------------------------
file_meta = Dataset()
file_meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.481.5"  # RT Plan Storage
file_meta.MediaStorageSOPInstanceUID = "1.2.3"
file_meta.ImplementationClassUID = "1.2.3.4"

# -----------------------------
# Create RTPLAN dataset
# -----------------------------
ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0" * 128)

# Date and time
dt = datetime.datetime.now()
ds.ContentDate = dt.strftime("%Y%m%d")
ds.ContentTime = dt.strftime("%H%M%S")

# -----------------------------
# Patient info
# -----------------------------
ds.PatientName = "TEST^PATIENT"
ds.PatientID = "123456"

# -----------------------------
# Plan info
# -----------------------------
ds.RTPlanLabel = "FAKE_PLAN"
ds.RTPlanDate = ds.ContentDate
ds.RTPlanTime = ds.ContentTime

# -----------------------------
# Beam sequence
# -----------------------------
beam = Dataset()
beam.BeamName = "ARC1"
beam.BeamNumber = 1
beam.NumberOfControlPoints = 2

# Control point sequence
cp = Dataset()
cp.GantryAngle = 180.0

beam.ControlPointSequence = [cp]

ds.BeamSequence = [beam]

# -----------------------------
# Save file
# -----------------------------
os.makedirs("../data", exist_ok=True)
ds.save_as(filename)

print("Fake RTPLAN created successfully")
print("Saved at:", filename)