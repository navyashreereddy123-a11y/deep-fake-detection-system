import utils

result = utils.predict("test.mp4")

print("Prediction:", result["label"])
print("Confidence:", result["confidence"])
print("Reason:", result["reason"])