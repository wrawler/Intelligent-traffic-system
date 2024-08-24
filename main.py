from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

results = model.track(source = '/media/test_footage/moving_traffic.mp4',show = True,tracker = "bytetrack.yaml")