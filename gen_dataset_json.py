from nnunet.dataset_conversion.utils import generate_dataset_json

generate_dataset_json("./dataset.json", "./imagesTr", "./imagesTs", modalities=("MRI", "noNorm", "noNorm", "noNorm"), labels={0:"background", 1:"RV", 2:"MYO", 3:"LV"}, dataset_name="ACDC-Phys")

