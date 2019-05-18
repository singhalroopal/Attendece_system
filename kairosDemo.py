import kairos_face as kf

# setting up keys
kf.settings.app_id = "a123a233"
kf.settings.app_key = "03a5065270150ba0e23a0584ae716b0d"

file_path = input("Image URL");

#enrolling new face
kf.enroll_face(file=file_path,subject_id = 's1',gallery_name = "test")

#detect face
print(kf.detect_face(file=file_path,gallery_name = "test"))