# Local Market Produce Annotation Pipeline – Batch 1

## Project Overview
This project involves **annotating real-world produce images** collected from local markets for four classes: **orange, pepper, tomato, and onion**.  
The dataset was created to demonstrate **multi-class, multi-instance object detection annotation skills** using **CVAT** and exported in **YOLO format**.  

It is intended as a **portfolio-ready dataset** to showcase annotation experience for remote image labeling projects.

---

## Dataset Details

- **Total Images:** 100  
- **Total Annotated Object Instances:** 669  
- **Classes and Instance Counts:**

| Class  | Instances |
|--------|----------|
| Orange | 81       |
| Pepper | 228      |
| Tomato | 207      |
| Onion  | 153      |

- **Average objects per image:** ~6–7  
- **Data type:** Raw images + YOLO annotation files  
- **Annotation format:** YOLO 1.1  

> Instance counts were derived by parsing YOLO annotation files (`.txt`), where each line represents one bounding box. Class IDs correspond to the labels defined in `obj.names`.

---

## Tools Used

- **CVAT** (Computer Vision Annotation Tool) for image annotation  
- **Docker** for running CVAT locally  
- **YOLO 1.1** for dataset export  

---

## Folder Structure

```text
fresh-produce-annotation-pipeline/
│
├── data/
│   ├── images/
│   │   └── batch_1/               ← Raw images
│   └── annotations/
│       └── batch_1_yolo/
│           ├── labels/            ← YOLO .txt files
│           └── obj.names          ← Class names
│
├── samples/
│   └── annotated_screenshots/     ← Screenshots from CVAT showing annotation quality
│
├── annotation_guidelines/
│   └── annotation_rules.md        ← Annotation rules and guidelines
│
├── README.md
└── requirements.txt