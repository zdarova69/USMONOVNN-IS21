from pixellib.instance import instance_segmentation


def object_detection_on_an_image():
    segment_image = instance_segmentation()
    segment_image.load_model("D:\project\mask_rcnn_coco.h5")
    
    segment_image.segmentImage(
        image_path="D:\project\index.jpg",
        output_image_name="D:\project\index.jpg"
        )

def main():
    object_detection_on_an_image()

if __name__ == '__main--':
    main
